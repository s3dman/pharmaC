from main import *

# def StockUpdate(db):
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