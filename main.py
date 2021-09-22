import pickle

# To read and write data into .DB files
def WriteDB(db,file):
    try:
        db_file = open(f'./database/{file}','wb')
        pickle.dump(db,db_file)
        db_file.close()
        return 0
    except IOError:
        return 1


def ReadDB(file):
    try:
        db_file = open(f'./database/{file}','rb')
        db = pickle.load(db_file)
        db_file.close()
        return db
    except IOError:
        return 1

def PP(db):
    for i in db:
        print(f"{i}:{db[i]}")
