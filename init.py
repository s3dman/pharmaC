from main import *
from billingpage import *
from management import *
from stock import *
from ui import *
from users import *
from authentication import Login

def initialize():
    counter = 5
    while counter>0:
        if Login() != -1:
            Clear()
            db = ReadDB('STOCK.DB')
            # LoadingScreen()
            HomePage(db)
            break
        else:
            counter -= 1
            if counter != 0:
                print(f"Password incorrect! {counter} attempts remaining.")
initialize()
