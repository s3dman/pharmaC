from main import ReadDB

def Login():
    passfile = ReadDB('MANAGEMENT.DB')
    x = input("Please enter admin password: ")
    if x.strip() == passfile['password']:
        return 0
    return -1
