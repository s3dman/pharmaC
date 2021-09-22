import pickle

# To read and write data into .DB files
def WriteDB(db,file):
    with open(f'./database/{file}','wb') as db_file:
        pickle.dump(db,db_file)

def ReadDB(file):
    with open(f'./database/{file}','rb') as db_file:
        db = pickle.load(db_file)
        return db

def PP(db):
    for i in db:
        print(f"{i}:{db[i]}")
