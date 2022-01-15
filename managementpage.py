from os import system, name
from main import ReadDB,WriteDB
from authentication import Encoder, Decoder

def Clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')
    # print("\n"*45)

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
    Clear()
    def takeinput():
        x = input("❯ ")
        if x in "1 2 0".split():
            if x == '1':
                TaxUpdate()
            if x == '2':
                PasswordUpdate()
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
                "1,Edit tax value".split(','),
                "2,Change access password".split(','),
                "0,Go back".split(','),
            ],
            linesbetweenrows=True,
        )
        if takeinput() == -1:
            Clear()
            break
        Clear()

def TaxUpdate():
    Clear()
    dbfile = ReadDB('MANAGEMENT.DB')
    tabulate(
        "Option Service".split(),
        [
            ["Old tax value",dbfile["tax"]],
        ],
        printheader=False
    )
    while True:
        tax = input("Input new tax percentage value: ")
        if tax.isnumeric():
            tax = int(tax)
            break
        else:
            print("Invalid syntax, Try again:")

    dbfile['tax'] = tax
    tabulate(
        "Option Service".split(),
        [
            ["New tax value",dbfile["tax"]],
        ],
        printheader=False
    )
    input("Press Enter to continue.")
    WriteDB(dbfile,'MANAGEMENT.DB')


def PasswordUpdate():
    Clear()
    dbfile = ReadDB('MANAGEMENT.DB')
    tabulate(
        "Option Service".split(),
        [
            ["Old password",Decoder(dbfile["password"])],
        ],
        printheader=False
    )
    pas = input("Input new password: ")

    dbfile['password'] = Encoder(pas)
    tabulate(
        "Option Service".split(),
        [
            ["New password",Decoder(dbfile["password"])],
        ],
        printheader=False
    )
    input("Press Enter to continue.")
    WriteDB(dbfile,'MANAGEMENT.DB')
