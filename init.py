from main import *
from billingpage import *
from management import *
from stock import *
from ui import *
from users import *
from authentication import Login

# start database and authentication and proceed to loadingscreen & homepage if passed
def initialize():
    counter = 5
    while counter>0:
        if Login() != -1:
            Clear()
            db = ReadDB('STOCK.DB')
            LoadingScreen()
            HomePage(db)
            return 0
        else:
            counter -= 1
            if counter != 0:
                print(f"Password incorrect! {counter} attempts remaining.")
    return 0

# to avoid initialization call when externally importing
# to be executed only when directly run 
if __name__ == "__main__":
    initialize()
