from main import *
import csv

# def UpdateDB(from_db,to_db):
    # Update stock from existing db
    # Abhi and John
# Exit code 0: no error, 1: does not exist, 2: insufficent qty
def ItemAdd(id,qty,db):
    if id in db.keys():
        db[id][1] += qty
        return 0
    return 1

def ItemRemove(id,qty,db):
    if id in db.keys():
        if db[id][1] < qty:
            return 2
        else:
            db[id][1] -= qty
            return 0
    return 1

def ReadStockFile(file):
    data = []
    data_dict = {}
    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for i in reader:
            data.append(i)
    for i in data:
        data_dict[i[0].strip()] = [i[1].strip(),int(i[2].strip()),int(i[3].strip())]
    return data_dict