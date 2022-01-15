import csv
import datetime

# helper function to sort date
def DateSorter(date):
    date = [int(i) for i in date[0].split('-')]
    return (date[1]*100)+date[0]

# to check if a date is expired by comparing with current date
def IsExpired(date) :
    td = datetime.date.today()
    d = [int(i) for i in date.split('-')]
    if d[1]<td.year:
        return True
    if d[1] == td.year and d[0]<=td.month:
        return True
    return False

# get dict of expired stuff from db
def GetExpired(db):
    expireddb = {}
    for ID in db:
        x = {}
        for i in db[ID][1]:
            if IsExpired(i):
                x.update({i:db[ID][1][i]})
        expireddb.update({ID:[db[ID][0],x]})
    return expireddb

# remove all expired stuff from db
def RemoveExpired(db):
    for ID in db:
        temp = db[ID][1].copy()
        for i in db[ID][1]:
            if IsExpired(i):
                del temp[i]
        db[ID][1] = temp

# remove all drug entries with qty<=0 from db
def CleanDB(db):
    for item_id in db:
        for i in list(db[item_id][1].items()):
            if i[1] <= 0:
                del db[item_id][1][i[0]]
    for j in list(db.items()):
        if j[1][1] == {}:
            del db[j[0]]

# add single item to db
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

# remove single item from db
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

# adds a dict of items (existant & non-existant) items to to_dict
def BulkAdd(from_dict,to_dict):
    for i in from_dict:
        ItemAdd(i,from_dict[i],to_dict)

# removes a dict of items (existant) from to_dict
# returns a list with dicts of expiry:qty if the item exists else -1
def BulkRemove(from_dict,to_dict):
    rlist = []
    for i in from_dict:
        if i in to_dict:
            rlist.append([i,to_dict[i][0],to_dict[i][-1],ItemRemove(i,from_dict[i][1],to_dict)])
    return rlist

# Read csv file and return a dict of items. different types of dicts are
# returned based on row length. if invalid csv is passed returns -1
def ReadBulkFile(file):
    data = []
    data_dict = {}
    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile)
        try:
            column_len = len(next(reader))
        except StopIteration:
            return -1
        for i in reader:
            data.append([int(j) if j.strip().isnumeric() else j.strip() for j in i])
        if column_len == 5:
            for i in data:
                data_dict[i[0]] = [i[1],{i[3]:i[2]},i[4]]
        elif column_len == 3:
            for i in data:
                data_dict[i[0]] = [i[1],i[2]]
        else:
            data_dict = -1
    return (column_len,data_dict)