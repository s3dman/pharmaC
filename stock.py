from main import *
import csv

#   Helper Functions
def DateSorter(date):
    date = [int(i) for i in date[0].split('-')]
    return (date[1]*100)+date[0]

def CleanDB(db):
    for item_id in db:
        for i in list(db[item_id][1].items()):
            if i[1] == 0:
                del db[item_id][1][i[0]]
    for j in list(db.items()):
        if j[1][1] == {}:
            del db[j[0]]

#   Add single item to db
def ItemAdd(item_id,item_info,db):
    if item_id in db:
        for i in item_info[1]:
            if i in db[item_id][1]:
                db[item_id][1][i] += item_info[1][i]
            else:
                db[item_id][1][i] = item_info[1][i]
    else:
        db[item_id] = item_info
    for j in db:
        db[j][1] = dict(sorted(db[j][1].items(),key=DateSorter))

#   Remove single item from db
def ItemRemove(ID,qty,db):
    if ID in db:
        rdict = {}
        for i in db[ID][1]:
            if db[ID][1][i]<qty:
                rdict[i] = db[ID][1][i]
                qty -= db[ID][1][i]
                db[ID][1][i] = 0
            else:
                rdict[i] = qty
                db[ID][1][i] -= qty
                CleanDB(db)
                return rdict
        CleanDB(db)
        return rdict
    else:
        return -1

# There are differences between bulkadd and bulkremove dbs
# BulkAddDB has ID, Name, Qty, Expiry, Cost
# BulkRemoveDB has ID, Name, Qty
def BulkAdd(from_dict,to_dict):
    for i in from_dict:
        ItemAdd(i,from_dict[i],to_dict)

#   Returns a list with dicts of expiry:qty if the item exists else -1
def BulkRemove(from_dict,to_dict):
    rlist = []
    for i in from_dict:
        rlist.append(ItemRemove(i,from_dict[i][1],to_dict))
    return rlist

# Read csv file and return a dict return different types of dicts for add and remove
def ReadBulkFile(file,):
    data = []
    data_dict = {}
    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile)
        column_len = len(next(reader))
        for i in reader:
            data.append([int(j) if j.strip().isnumeric() else j.strip() for j in i])
        if column_len == 5:
            for i in data:
                data_dict[i[0]] = [i[1],{i[3]:i[2]},i[4]]
        else:
            for i in data:
                data_dict[i[0]] = [i[1],i[2]]
    return data_dict