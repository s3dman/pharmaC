import datetime

# get formatted date
def Today():
    today= datetime.datetime.now()
    return [today.strftime("%d-%m-%y"),today.strftime("%X")]

# add user logs (name,purchased items) to userlogdb
def AddUserLogs(name,purchase_list,userlogdb):
    name = name.strip().title()
    if Today()[0] in userlogdb:
        userlogdb[Today()[0]].update({Today()[1]:{name:purchase_list}})
    else:
        userlogdb[Today()[0]] = {Today()[1]:{name:purchase_list}}

# purchase_list is modified to a format which can be parsed for bill generation
def FinalBill(purchase_list,tax):
    totalcost = 0
    for i in purchase_list:
        count = 0
        for j in i[3]:
            count += i[3][j]
        costperitem = count*i[2]
        i.append(costperitem)
        totalcost += costperitem
    purchase_list.append([float(totalcost),float(totalcost)*tax/100])
    return purchase_list
