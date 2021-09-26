from management import SearchWithName
from ui import tabulate, Clear
from main import CheckLocalFiles
from stock import ReadBulkFile, BulkRemove
from users import FinalBill
from main import ReadDB
from pprint import pprint
import datetime

def PrimaryInput(db):

    drugslist = {}
    def DrugPrompt():
        Clear()
        def DrugNameInput():
            med = input("Drug name: ")
            templist = []
            for i in SearchWithName(med,db):
                qty = 0
                for j in db[i][1]:
                    qty += db[i][1][j]
                templist.append([len(templist)+1,i,db[i][0],qty])
            if len(templist) == 0:
                Clear()
                print("No Results Found")
                return DrugNameInput()
            return templist
        templist = DrugNameInput()
        Clear()
        print(f"{len(templist)} Results Found:")
        tabulate(
            "SNo.,ID,Name,Available".split(","),
            templist)

        def choicePrompt():
            choice = input(f"Enter your choice [1-{len(templist)}]:")
            if choice.isnumeric():
                choice = int(choice)
                if choice not in range(1,len(templist)+1):
                    print("Invalid input, try again")
                    return choicePrompt()
                else: return choice
            else:
                print("Invalid input, try again")
                return choicePrompt()

        drugindex = choicePrompt()-1  # relative inside templist
        print(f"You chose {templist[drugindex][2]}")

        def qtyPrompt():
            x = input("Enter quantity: ")
            if x.isnumeric():
                x = int(x)
                if x<=0:
                    print("Invalid input, try again")
                    return qtyPrompt()
                if x>templist[drugindex][-1]:
                    print(f"Not enough available, taking maximum available: {templist[drugindex][-1]}")
                    return templist[drugindex][-1]
                else:
                    return x
            else:
                print("Invalid input, try again")
                return qtyPrompt()
        inputqty = qtyPrompt()
        drugslist[templist[drugindex][1]] = [templist[drugindex][2],inputqty]


    # actual running here (above definitions)
    customer_name = input("Customer name: ")
    isbulk = input("Bulk order (y/n): ").lower()
    if isbulk == 'y':
        input("Place bulk order list file inside the FILES directory ")
        files = CheckLocalFiles()
        print(f"{len(files)} Results found:")
        tabulate(
            ["SNo.","File",],
            [[files.index(i)+1,i] for i in files],
            linesbetweenrows = True
        )

        def BulkPrompt():
            y = input(f"Enter your choice [1-{len(files)}]: ")
            if y.isnumeric():
                y = int(y)
                if y not in range(1,len(files)+1):
                    print("Invalid input, try again")
                    return BulkPrompt()
                else:
                    bulkdb = ReadBulkFile(f"FILES/{files[y-1]}")
                    if bulkdb != -1:
                        if bulkdb[0] == 3:
                            return files[y-1]
                        else:
                            print("Invalid file, try again")
                            return BulkPrompt()
                    else:
                        print("Invalid file, try again")
                        return BulkPrompt()
            else:
                print("Invalid input, try again")
                return BulkPrompt()
        filename = BulkPrompt()
        Clear()
        print(f"You have chosen {filename}")
        return [ReadBulkFile(f"FILES/{filename}")[1], customer_name]
    else:
        DrugPrompt()
        while True:
            prompt = input("Add more entries (y/n):").lower()
            if prompt == 'y':
                DrugPrompt()
            else:
                Clear()
                break
        return [drugslist,customer_name]

def FinalEditOption(db):
    temp,name = PrimaryInput(db)
    print("Order summary:")
    order_db = []
    for i in temp:
        order_db.append([len(order_db)+1,i,temp[i][0],temp[i][1]])
    tabulate(
    "Sno.,ID,Name,Quantity".split(","),
    order_db
    )
    needbulkchanges = input("Do you want to make any changes (y/n): ").lower()
    if needbulkchanges == 'y':
        def needchangeprompt():
            x = input(f"Which entry you want to change [1-{len(order_db)}]: ")
            if x.isnumeric():
                x = int(x)
                if x not in range(1,len(order_db)+1):
                    print("Invalid input, try again")
                    return needchangeprompt()
                return x
            else:
                print("Invalid input, try again")
                return needchangeprompt()

        def qtyPrompt(maxqty):
            x = input("Enter quantity: ")
            if x.isnumeric():
                x = int(x)
                if x<0:
                    print("Invalid input, try again")
                    return qtyPrompt(maxqty)
                if x==0:
                    # TODO
                    pass
                if x>maxqty:
                    print(f"Not enough available, taking maximum available: {maxqty}")
                    return maxqty
                else:
                    return x
            else:
                print("Invalid input, try again")
                return qtyPrompt(maxqty)

        while True:
            changeindex = needchangeprompt() - 1
            maxqtywehave = 0
            for i in db[order_db[changeindex][1]][1]:
                maxqtywehave += db[order_db[changeindex][1]][1][i]
            inputqty = qtyPrompt(maxqtywehave)
            print(f"Changed qty of {order_db[changeindex][2]} from {order_db[changeindex][-1]} to {inputqty}")
            temp[order_db[changeindex][1]][-1] = inputqty
            order_db[changeindex][-1] = inputqty
            prompt = input("Do you want to make any more changes (y/n): ").lower()
            if prompt == 'y':
                Clear()
                tabulate(
                "Sno.,ID,Name,Quantity".split(","),
                order_db
                )
            else:
                break
    Clear()
    print("Final order summary: ")
    tabulate(
    "Sno.,ID,Name,Quantity".split(","),
    order_db
    )
    x = input("Continue to Payment (y/n):").lower()
    if x == 'y':
        Clear()
        expblk = {}
        for i in order_db:
            expblk[i[1]] = i[2:]

        def billprint(header,data,Name,z,tax,printheader=True,linesbetweenrows=False,prependspace=0):
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
            print(prependspace*' '+"| Customer: "+Name+(wide-len(Name)-33)*' '+f"{' / '.join(str(datetime.datetime.now())[:-7].split())} |")
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

        expblk = BulkRemove(expblk,db)  # get the db with all info
        tax = ReadDB("MANAGEMENT.DB")['tax']
        finalbill = FinalBill(expblk,tax)
        x_X = ['SNo', 'ID', 'Item', 'Expiry', 'Quantity', 'Rate', 'Net Price']
        y_Y = []
        for i in finalbill[:-1]:
            temp = list(i[3].items())
            y_Y.append([finalbill.index(i)+1,i[0],i[1],temp[0][0],temp[0][1],i[2],i[-1]])
            for i in temp[1:]:
                y_Y.append(["","","",i[0],i[1],"",""])
            y_Y.append(["","","","","","",""])
        billprint(x_X,y_Y,name,finalbill[-1],tax)
        input("Press Enter to go to main menu")
    else:
        return
