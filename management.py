from main import *
from stock import *
from difflib import SequenceMatcher
import datetime

def ManualEdit(ID,db,name=-1,cost=-1):
    if name != -1:
        db[ID][0] = name
    if cost != -1:
        db[ID][-1] = cost

def SearchWithName(name,db):
    similar = []
    for i in db:
        if SequenceMatcher(None,name,db[i][0]).ratio() >= 0.6:
            similar.append(i)
    return similar

def GlobalValueUpdater(valuedb,db):
    db.update(valuedb)

def Logger(msg):
    with open('database/database.log','a') as file:
        file.write(f"[{datetime.datetime.now()}] {msg}\n")
