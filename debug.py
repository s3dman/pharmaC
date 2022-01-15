# debug script for running unit tests

from main import ReadDB, WriteDB

def setupnew():
    WriteDB({},'USERS.DB')
    WriteDB({},'STOCK.DB')
    WriteDB({'tax':0,'password':'�100�114�111�119�115�115�97�112'},'MANAGEMENT.DB')