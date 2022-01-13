from os import system, name
import datetime
from main import ReadDB

def Clear():
    # if name == 'nt': _ = system('cls')
    # else: _ = system('clear')
    print("\n"*45)

def tabulate(header,data,printheader=True,linesbetweenrows=False,prependspace=0):
    widths = [len(cell) for cell in header]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])
    formatted_row = ' | '.join('{:%d}' % width for width in widths)
    if printheader:
        print(prependspace*' '+'+'+'-'*(len(formatted_row.format(*header))+2)+'+')
        print(prependspace*' '+'| '+formatted_row.format(*header)+' |')
        print(prependspace*' '+'+'+'='*(len(formatted_row.format(*header))+2)+'+')
    else:
        print(prependspace*' '+'+'+'-'*(len(formatted_row.format(*header))+2)+'+')
    for row in data:
        print(prependspace*' '+'| '+formatted_row.format(*row)+' |')
        if linesbetweenrows:
            print(prependspace*' '+'+'+'-'*(len(formatted_row.format(*header))+2)+'+')
    if linesbetweenrows == False: print(prependspace*' '+'+'+'-'*(len(formatted_row.format(*header))+2)+'+')

def MainPage():
    userdb = ReadDB('USERS.DB')
    Clear()
    def takeinput():
        x = input("❯ ")
        if x in "1 2 3 0".split():
            if x == '1':
                SearchByUser(userdb)
            if x == '2':
                SearchByDate(userdb)
            if x == '0':
                return -1
        else:
            print("Invalid syntax, Try again:")
            takeinput()
    while True:
        print("Type the option you want to choose and press Enter [0-2]:")
        tabulate(
            "Option Service".split(),
            [
                "1,Search by User".split(','),
                "2,Search by Date".split(','),
                "0,Go back".split(','),
            ],
            linesbetweenrows=True,
        )
        if takeinput() == -1:
            Clear()
            break
        Clear()

def SearchByUser(udb):
    Clear()
    username = input('Enter Username that you want to check: ').title()
    templist = []
    date_list = []
    for i in udb.items():
        for j in i[1].items():
            for k in j[1].items():
                if k[0] == username:
                    templist.append(k[1])
                    date_list.append([i[0],j[0]])
    if len(templist) == 0:
        print(f"No Transactions available for {username}.")
    else:
        print(f"{len(templist)} Transactions found: ")
    counter = 0
    for finalbill in templist:
        tax = ReadDB("MANAGEMENT.DB")['tax']
        x_X = ['SNo', 'ID', 'Item', 'Expiry', 'Quantity', 'Rate', 'Net Price']
        y_Y = []
        for i in finalbill[:-1]:
            temp = list(i[3].items())
            y_Y.append([finalbill.index(i)+1,i[0],i[1],temp[0][0],temp[0][1],i[2],i[-1]])
            for i in temp[1:]:
                y_Y.append(["","","",i[0],i[1],"",""])
            y_Y.append(["","","","","","",""])
        billprint(x_X,y_Y,username,finalbill[-1],tax,date_list[counter])
        counter += 1
        print()
    input("Press Enter to continue.")

def SearchByDate(udb):
    date = input('Enter date that you want to check[dd-mm-yy]: ')
    namelist = []
    billlist = []
    date_list = []
    for i in udb.items():
        if i[0] == date:
            for j in i[1].items():
                for k in j[1].items():
                    namelist.append(k[0])
                    billlist.append(k[1])
                    date_list.append([i[0],j[0]])
    if len(namelist) == 0:
        print(f"No Transactions available for {date}.")
    else:
        print(f"{len(namelist)} Transactions found: ")
    for k in range(len(namelist)):
        finalbill=billlist[k]
        username=namelist[k]
        tax = ReadDB("MANAGEMENT.DB")['tax']
        x_X = ['SNo', 'ID', 'Item', 'Expiry', 'Quantity', 'Rate', 'Net Price']
        y_Y = []
        for i in finalbill[:-1]:
            temp = list(i[3].items())
            y_Y.append([finalbill.index(i)+1,i[0],i[1],temp[0][0],temp[0][1],i[2],i[-1]])
            for i in temp[1:]:
                y_Y.append(["","","",i[0],i[1],"",""])
            y_Y.append(["","","","","","",""])
        billprint(x_X,y_Y,username,finalbill[-1],tax,date_list[k])
        print()
    input("Press Enter to continue.")

def billprint(header,data,Name,z,tax,dat,printheader=True,prependspace=0):
    widths = [len(cell) for cell in header]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])
    formatted_row = ' | '.join('{:%d}' % width for width in widths)
    wide = len('-'*(len(formatted_row.format(*header))+2))
    print(prependspace*' '+'+'+'='*(len(formatted_row.format(*header))+2)+'+')
    print(prependspace*' '+"|"+"SED Pharma".center(wide," ")+"|")
    print(prependspace*' '+"|"+"~~~~~~~~~~".center(wide," ")+"|")
    # print(prependspace*' '+"|"+wide*" "+"|")
    print(prependspace*' '+"| Customer: "+Name+(wide-len(Name)-33)*' '+f"  {' / '.join(dat)} |")
    if printheader:
        print(prependspace*' '+'+'+'-'*(len(formatted_row.format(*header))+2)+'+')
        print(prependspace*' '+'| '+formatted_row.format(*header)+' |')
        print(prependspace*' '+'+'+'='*(len(formatted_row.format(*header))+2)+'+')
    else:
        print(prependspace*' '+'+'+'-'*(len(formatted_row.format(*header))+2)+'+')
    endcounter = 0
    for row in data:
        endcounter += 1
        if row[3] == "":
            if endcounter == len(data):
                continue
            print(prependspace*' '+'+'+'-'*(len(formatted_row.format(*header))+2)+'+')
            continue
        print(prependspace*' '+'| '+formatted_row.format(*row)+' |')
    print(prependspace*' '+'+'+'='*(len(formatted_row.format(*header))+2)+'+')
    print(prependspace*" "+"| Total cost before Tax:"+" "*(wide-27-len(str(z[0])))+f"Rs {z[0]} |")
    print(prependspace*" "+f"| Tax [{tax}%]:"+" "*(wide-15-len(str(z[1])))+f"Rs {z[1]} |")
    print(prependspace*" "+"| Total cost after Tax:"+" "*(wide-26-len(str(z[1]+z[0])))+f"Rs {z[1]+z[0]} |")
    print(prependspace*' '+'+'+'='*(len(formatted_row.format(*header))+2)+'+')

