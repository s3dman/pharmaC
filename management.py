from difflib import SequenceMatcher
import datetime

# manually edit name/cost of a drug from a db
def ManualEdit(ID,db,name=-1,cost=-1):
    if name != -1:
        db[ID][0] = name
    if cost != -1:
        db[ID][-1] = cost

# sequence matching search to find similar drug names
def SearchWithName(name,db):
    similar = []
    for i in db:
        if SequenceMatcher(None,name,db[i][0]).ratio() >= 0.6:
            similar.append(i)
    return similar

# logger function
def Logger(msg):
    with open('database/database.log','a') as file:
        file.write(f"[{datetime.datetime.now()}] {msg}\n")
