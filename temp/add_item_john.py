from main import *


def med_to_update(serial_no:str,qty:int):
    a = serial_no
    if a in stock_db.keys():
        stock_db[a]['qty'] = stock_db[a]['qty'] + qty
        return stock_db[serial_no]['qty']
    else:
        print("Item doesn't exist")


print("pls select the item u want from the list below:")
for x,y in stock_db.items():
    print(x,y)

while True:
    item = input()

    if item in stock_db.keys():
        print(stock_db[str(item)])
        print("How much more medicines do you want to add?")
        quantity = input()
        print(f"There is now {med_to_update(item, int(quantity))} {stock_db[item]['name']}")
        break
    else:
        print("Item doesn't exist, Please Try again")
        continue
