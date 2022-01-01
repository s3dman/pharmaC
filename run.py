from main import *
from billingpage import *
from management import *
from stock import *
from ui import *
from users import *

db = ReadDB('STOCK.DB')
# LoadingScreen()
HomePage(db)
