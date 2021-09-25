from management import SearchWithName
from ui import tabulate, Clear
from main import CheckLocalFiles
from stock import ReadBulkFile

def primaryinput(db):

    drugslist = {}
    def DrugPrompt():
        Clear()
        med = input("Drug name: ")
        templist = []
        for i in SearchWithName(med,db):
            qty = 0
            for j in db[i][1]:
                qty += db[i][1][j]
            templist.append([len(templist)+1,i,db[i][0],qty])
        if len(templist) <= 0:
            print("No Results Found")
        else:
            print("Results:")
            tabulate(
                "SNo.,ID,Name,Available".split(","),
                templist)

            def choicePrompt():
                choice = input("Enter your choice: ")
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
        input("Place bulk order list file inside the FILES directory")
        files = CheckLocalFiles()
        tabulate(
            [f"Found {len(files)} files",],
            [[i,] for i in files],
            linesbetweenrows = True
        )

        def BulkPrompt():
            y = input("Enter your choice: ")
            if y.isnumeric():
                y = int(y)
                if y not in range(1,len(files)+1):
                    print("Invalid input, try again")
                    return BulkPrompt()
                else: return y
            else:
                print("Invalid input, try again")
                return BulkPrompt()
        bulkindex = BulkPrompt() - 1
        print(f"You have chosen {files[bulkindex]}")
        return ReadBulkFile(f"FILES/{files[bulkindex]}")

    else:
        DrugPrompt()
        while True:
            prompt = input("Add more entries (y/n):").lower()
            if prompt == 'y':
                DrugPrompt()
            else: break
        return drugslist
