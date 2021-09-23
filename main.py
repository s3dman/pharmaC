import pickle
import datetime

# To read and write data into .DB files
def WriteDB(db,file):
    with open(f'./database/{file}','wb') as db_file:
        pickle.dump(db,db_file)

def ReadDB(file):
    with open(f'./database/{file}','rb') as db_file:
        db = pickle.load(db_file)
        return db

def IsExpired(date):
    td = datetime.date.today()
    d = [int(i) for i in date.split('-')]
    if d[1]<td.year:
        return True
    if d[1] == td.year and d[0]<=td.month:
        return True
    return False

def PP(db):
    for i in db:
        print(f"{i}:{db[i]}")
