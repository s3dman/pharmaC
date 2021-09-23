from main import *
from stock import *
from difflib import SequenceMatcher

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
