from os import system, name
from management import SearchWithName

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
        if x in "1 2 3 0".split():
            if x == '1':
                SearchAndEditPage(db)
            if x == '2':
                pass
            if x == '3':
                pass
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
                "2,Bulk Add".split(','),
                "3,Expired".split(','),
                "0,Go back".split(','),
            ],
            linesbetweenrows=True,
        )
        if takeinput() == -1:
            Clear()
            break
        Clear()

def SearchAndEditPage(db):
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

    DrugPrompt()
    while True:
        prompt = input("Edit more entries (y/n):").lower()
        if prompt == 'y':
            DrugPrompt()
        else:
            Clear()
            break
    print(drugslist)
    input()
    
def BulkAdd():
    pass

def Expired():
    pass
