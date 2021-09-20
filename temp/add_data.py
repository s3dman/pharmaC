from main import *

for x,y in stock_db.items():
    print(x,y)

for i in stock_update_db.keys():
    if i in stock_db.keys():
        stock_db[i]['qty'] = stock_db[i]['qty'] + stock_update_db[i]['qty']

print()
for x,y in stock_db.items():
    print(x,y)