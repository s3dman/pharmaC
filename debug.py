from main import *
from billingpage import *
from management import *
from stock import *
from ui import *
from users import *
from reportpage import SalesGraph

userdb = ReadDB('USERS.DB')
SalesGraph(userdb)