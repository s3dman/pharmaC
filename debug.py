# debug script for running unit tests

import run
import init
import authentication
import main
import management
import stock
import users
import ui
import userhistorypage
import managementpage
import reportpage
import billingpage
import inventorypage
import debug

userdb = main.ReadDB('USERS.DB')
managementdb = main.ReadDB('MANAGEMENT.DB')
stockdb = main.ReadDB('STOCK.DB')

reportpage.SalesGraph(userdb)