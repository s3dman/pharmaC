# debug script for running unit tests

from pprint import pprint

from main import ReadDB, WriteDB

userdb = ReadDB('USERS.DB')
managementdb = ReadDB('MANAGEMENT.DB')
stockdb = ReadDB('STOCK.DB')
# WriteDB({},'USERS.DB')
# WriteDB({},'STOCK.DB')
WriteDB({'tax':0,'password':'�100�114�111�119�115�115�97�112'},'MANAGEMENT.DB')
managementdb = ReadDB('MANAGEMENT.DB')

# pprint(userdb)
pprint(managementdb)
pprint(stockdb)