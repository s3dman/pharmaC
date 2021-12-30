from main import ReadDB
from os import system, name

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
    
def BarGrapher(data_):
    Clear()
    data = {}
    maxlen = max(len(i) for i in data_)
    mindata = min(data_.values())
    maxdata = max(data_.values())
    for i in data_:
        data[i] = int((74-maxlen)*(data_[i]-mindata+1)/(maxdata-mindata+1))
        if data[i] <= 0:
            data[i] = 1
    # print('+'+'-'*80+'+')
    print('+'+'-'*(maxlen+2)+'+'+(77-maxlen)*'-'+'+')
    for i in data:
        print('| '+i.rjust(maxlen)+' | '+"█"*data[i]+" "*(76-maxlen-data[i])+'|')
        print('+'+'-'*(maxlen+2)+'+'+(77-maxlen)*'-'+'+')
    input("Press Enter to continue.")


def MainPage():
    temp_db={}
    userdb = ReadDB('USERS.DB')
    for i in userdb.items():
        for j in i[1].items():
            for k in j[1].items():
                for l in k[1][:-1]:
                    if l[1] in temp_db:
                        temp_db[l[1]] += l[-1]
                    else:
                        temp_db.update({l[1]:l[-1]})
    Clear()
    def takeinput():
        x = input("❯ ")
        if x in "1 2 0".split():
            if x == '1':
                BarGrapher(temp_db)
            if x == '2':
                pass
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
                "1,Drug sales chart".split(','),
                "2,Sales Report".split(','),
                "0,Go back".split(','),
            ],
            linesbetweenrows=True,
        )
        if takeinput() == -1:
            Clear()
            break
        Clear()
