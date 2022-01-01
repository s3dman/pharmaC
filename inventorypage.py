from os import system, name
from pprint import pprint
from management import SearchWithName
from main import ReadDB,WriteDB

def Clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

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

def MainPage(db):
    Clear()
    def takeinput():
        x = input("❯ ")
        if x in "1 2 3 4 0".split():
            if x == '1':
                SearchAndEditPage(db)
            if x == '2':
                # view fuill db
                pass
            if x == '3':
                # bulk add
                pass
            if x == '0':
                # search and delete/export expired
                return -1
        else:
            print("Invalid syntax, Try again:")
            takeinput()
    while True:
        print("Type the option you want to choose and press Enter [0-3]:")
        tabulate(
            "Option Service".split(),
            [
                "1,Search and Edit".split(','),
                "2,View Inventory".split(','),
                "3,Bulk add".split(','),
                "4,Expired".split(','),
                "0,Go back".split(','),
            ],
            linesbetweenrows=True,
        )
        if takeinput() == -1:
            Clear()
            break
        Clear()

        # WriteDB(db,'STOCK.DB')
        # TODO write important


def SearchAndEditPage(db):
    def DrugPrompt():
        Clear()
        def DrugNameInput():
            med = input("Drug name: ")
            templist = []
            for i in SearchWithName(med,db):
                templist.append([len(templist)+1,i,db[i][0]])
            if len(templist) == 0:
                Clear()
                print("No Results Found")
                return DrugNameInput()
            return templist
        templist = DrugNameInput()
        Clear()
        print(f"{len(templist)} Results Found:")
        tabulate(
            "SNo.,ID,Name".split(","),
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
        Clear()
        print(f"You chose {templist[drugindex][2]}")

        # Operation prompt
        Clear()
        def nameEdit():
            dat = db[templist[drugindex][1]]
            Clear()
            tabulate(
                "Option Value".split(),
                [
                    ["Old Name",dat[0]],
                ],
                printheader=False
            )
            while True:
                newname = input("Input new name: ")
                if newname.isalnum():
                    break
                else:
                    print("Invalid syntax, Try again:")
            dat[0] = newname.strip()
            tabulate(
                "Option Value".split(),
                [
                    ["New Name",dat[0]],
                ],
                printheader=False
            )
            input("Press Enter to continue.")

        def qtyEdit():
            dat = db[templist[drugindex][1]]
            exp_list = []
            qty_counter = 1
            for i in dat[1].items():
                exp_list.append([qty_counter,i[0],i[1]])
                qty_counter += 1
            tabulate(
                "Sno Expiry Qty".split(),
                exp_list,
                linesbetweenrows=True,
            )
            while True:
                choice = input(f"Enter your choice [1-{len(exp_list)}]: ")
                if choice.isnumeric() and int(choice)>0 and int(choice)<len(exp_list)+1:
                    choice = int(choice)
                    break
                print("Invalid syntax, Try again:")
            tabulate(
                "Option Value".split(),
                [
                    ["Old Qty",exp_list[choice-1][2]],
                ],
                printheader=False
            )
            while True:
                newqty = input("Input new Qty: ")
                if newqty.isnumeric():
                    break
                else:
                    print("Invalid syntax, Try again:")
            
            # debugging
            print(dat)
            input()
            # TODO change qty in main db
            exp_list[choice-1][2] = int(newqty)
            tabulate(
                "Option Value".split(),
                [
                    ["New Qty",exp_list[choice-1][2]],
                ],
                printheader=False
            )
            input("Press Enter to continue.")
            return -1
            

        def takeinput():
            x = input("❯ ")
            if x in "1 2 3".split():
                if x == '1':
                    return nameEdit()
                if x == '2':
                    return qtyEdit()
                if x == '3':
                    pass
            else:
                print("Invalid syntax, Try again:")
                takeinput()
        while True:
            print("Type the option you want to edit and press Enter [0-3]:")
            tabulate(
                "Option Value".split(),
                [
                    "1,Name".split(','),
                    "2,Qty".split(','),
                    "3,Price".split(','),
                ],
                linesbetweenrows=True,
            )
            if takeinput() == -1:
                Clear()
                break
            Clear()

    # actual running here
    DrugPrompt()
    
def BulkAdd():
    pass

def Expired():
    pass

def WholeInventory():
    pass
