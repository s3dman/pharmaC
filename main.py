import pickle

# To read and write data into .DB files
def WriteDB(db,file):
    db_file = open(f'./database/{file}','wb')
    pickle.dump(db,db_file)
    db_file.close()

def ReadDB(file):
    db_file = open(f'./database/{file}','rb')
    db = pickle.load(db_file)
    db_file.close()
    return db

def PP(db):
    for i in db:
        print(f"{i}:{db[i]}")
