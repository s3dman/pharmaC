from main import *
from stock import *
import datetime

def Today():
    today= datetime.datetime.now()
    return [today.strftime("%d-%m-%y"),today.strftime("%X")]

def FinalBill(purchase_list,main_db,tax):
    totalcost = 0
    for i in purchase_list:
        count = 0
        for j in i[1]:
            count += i[1][j]
        costperitem = count*main_db[i[0]][-1]
        i.append(costperitem)
        totalcost += costperitem
    purchase_list.append([totalcost,totalcost*tax])
    return purchase_list

def AddUserLogs(name,purchase_list,userlogdb):
    name = name.strip().title()
    if Today()[0] in userlogdb:
        userlogdb[Today()[0]].update({Today()[1]:{name:purchase_list}})
    else:
        userlogdb[Today()[0]] = {Today()[1]:{name:purchase_list}}