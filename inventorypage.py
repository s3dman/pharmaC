from os import system, name
from pprint import pprint
from management import SearchWithName
from main import ReadDB,WriteDB
from stock import ReadBulkFile, BulkAdd as BulkAddToDB, GetExpired, RemoveExpired, CleanDB
from main import CheckLocalFiles

def Clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

# modifed tabulate function for this use case
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

# inventory page main menu
def MainPage(db):
    Clear()
    def takeinput():
        x = input("❯ ")
        if x in "1 2 3 4 0".split():
            if x == '1':
                SearchAndEditPage(db)
            if x == '2':
                WholeInventory(db)
            if x == '3':
                BulkAdd(db)
            if x == '4':
                Expired(db)
            if x == '0':
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

        WriteDB(db,'STOCK.DB')

# search for drug and edit variables
def SearchAndEditPage(db):
    def DrugPrompt():
        Clear()
        # sequence matched drug name prompt
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

        # choice prompt for all entries from DrugNameInput
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

        # operation prompt
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

        # quantity edit option for selected drug
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
            
            dat[1][exp_list[choice-1][1]] = int(newqty)

            tabulate(
                "Option Value".split(),
                [
                    ["New Qty",dat[1][exp_list[choice-1][1]]],
                ],
                printheader=False
            )
            input("Press Enter to continue.")
            return -1

        # price edit option for selected drug
        def priceEdit():
            dat = db[templist[drugindex][1]]
            Clear()
            tabulate(
                "Option Value".split(),
                [
                    ["Old Price",dat[2]],
                ],
                printheader=False
            )
            while True:
                newname = input("Input new price: ")
                if newname.isnumeric():
                    break
                else:
                    print("Invalid syntax, Try again:")
            dat[2] = int(newname)
            tabulate(
                "Option Value".split(),
                [
                    ["New price",dat[2]],
                ],
                printheader=False
            )
            input("Press Enter to continue.")

        # menu for variable edit option
        def takeinput():
            x = input("❯ ")
            if x in "1 2 3".split():
                if x == '1':
                    return nameEdit()
                if x == '2':
                    return qtyEdit()
                if x == '3':
                    return priceEdit()
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
    
# parser function before using BulkAdd to db function
def BulkAdd(db):
    # list local available files
    Clear()
    input("Place bulk import file inside the FILES directory ")
    files = CheckLocalFiles()
    print(f"{len(files)} Results found:")
    tabulate(
        ["SNo.","File",],
        [[files.index(i)+1,i] for i in files],
        linesbetweenrows = True
    )

    # prompt for chosing local files
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
                    if bulkdb[0] == 5:
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
    adddb = ReadBulkFile(f"FILES/{filename}")[1] # ignore linter
    temp_list = []
    counter = 0
    for i in adddb:
        for j in adddb[i][1]:
            temp_list.append([counter+1,i,adddb[i][0],j,adddb[i][1][j],adddb[i][-1]])
        counter += 1
    tabulate("SNo ID Name Expiry Qty Cost".split(),temp_list)
    # actually adding to DB
    BulkAddToDB(adddb,db)
    input(f"Successfully added {len(adddb)} items. Press Enter to continue.")

# print out the whole inventory with details
def WholeInventory(db):
    Clear()
    header = "ID Name Expiry Qty Cost".split()
    data = []
    for i in db.items():
        curstuf = list(i[1][1].items())
        data.append([i[0],i[1][0],curstuf[0][0],str(curstuf[0][1]),i[1][-1]])
        for j in curstuf[1:]:
            data.append([" "," ",j[0],str(j[1])," "])

    widths = [len(cell) for cell in header]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])
    formatted_row = ' | '.join('{:%d}' % width for width in widths)
    wide = len('-'*(len(formatted_row.format(*header))+2))
    print('+'+'='*(len(formatted_row.format(*header))+2)+'+')
    print("|"+"Inventory".center(wide," ")+"|")
    print('+'+'-'*(len(formatted_row.format(*header))+2)+'+')
    print('| '+formatted_row.format(*header)+' |')
    print('+'+'='*(len(formatted_row.format(*header))+2)+'+')
    print('| '+formatted_row.format(*data[0])+' |')
    for row in data[1:-1]:
        if row[0] == " ":
            print('| '+formatted_row.format(*row)+' |')
        else:
            print('+'+'-'*(len(formatted_row.format(*header))+2)+'+')
            print('| '+formatted_row.format(*row)+' |')
    if data[-1][0] == " ":
        print('| '+formatted_row.format(*data[-1])+' |')
    else:
        print('+'+'-'*(len(formatted_row.format(*header))+2)+'+')
        print('| '+formatted_row.format(*data[-1])+' |')
    print('+'+'='*(len(formatted_row.format(*header))+2)+'+')

    input("Press Enter to continue.")

# expired remove ui
def Expired(db):
    to_be_removed = GetExpired(db)
    Clear()
    header = "ID Name Expiry Qty".split()
    data = []
    for i in to_be_removed.items():
        curstuf = list(i[1][1].items())
        data.append([i[0],i[1][0],curstuf[0][0],str(curstuf[0][1])])
        for j in curstuf[1:]:
            data.append([" "," ",j[0],str(j[1])])
    widths = [len(cell) for cell in header]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])
    formatted_row = ' | '.join('{:%d}' % width for width in widths)
    wide = len('-'*(len(formatted_row.format(*header))+2))
    print('+'+'='*(len(formatted_row.format(*header))+2)+'+')
    print("|"+"Expired".center(wide," ")+"|")
    print('+'+'-'*(len(formatted_row.format(*header))+2)+'+')
    print('| '+formatted_row.format(*header)+' |')
    print('+'+'='*(len(formatted_row.format(*header))+2)+'+')
    print('| '+formatted_row.format(*data[0])+' |')
    for row in data[1:-1]:
        if row[0] == " ":
            print('| '+formatted_row.format(*row)+' |')
        else:
            print('+'+'-'*(len(formatted_row.format(*header))+2)+'+')
            print('| '+formatted_row.format(*row)+' |')
    if data[-1][0] == " ":
        print('| '+formatted_row.format(*data[-1])+' |')
    else:
        print('+'+'-'*(len(formatted_row.format(*header))+2)+'+')
        print('| '+formatted_row.format(*data[-1])+' |')
    print('+'+'='*(len(formatted_row.format(*header))+2)+'+')

    # confirmation menu for removal
    while True:
        x = input("Proceed to removal [y/n]: ")
        if x in "Yy":
            RemoveExpired(db)
            print(f"removed {len(data)} entries.")
            break
        elif x in "Nn":
            print("No entries removed.")
            break
        else:
            print("Invalid syntax, Try again:")
    CleanDB(db)
    input("Press Enter to continue.")
