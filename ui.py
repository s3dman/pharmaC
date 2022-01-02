import time
from os import system, name

import billingpage
from main import WriteDB
import inventorypage
import userhistorypage
import reportpage
import managementpage

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


def LoadingScreen():
    Prepend = ' '*8
    for i in range(58):
        print(f"""
{Prepend} ____   _____  ____      ____   _
{Prepend}/ ___| | ____||  _ \    |  _ \ | |__    __ _  _ __  _ __ ___    __ _
{Prepend}\___ \ |  _|  | | | |   | |_) || '_ \  / _` || '__|| '_ ` _ \  / _` |
{Prepend} ___) || |___ | |_| |   |  __/ | | | || (_| || |   | | | | | || (_| |
{Prepend}|____/ |_____||____/    |_|    |_| |_| \__,_||_|   |_| |_| |_| \__,_|\n\n""")
        print(f"{Prepend}LOADING: [{'#'*i+' '*(58-i)}]")
        time.sleep(0.05)
        Clear()

def HomePage(db):
    def takeinput():
        x = input("❯ ")
        if x in "1 2 3 4 5 0".split():
            if x == '1':
                Clear()
                billingpage.FinalEditOption(db)
            if x == '2':
                inventorypage.MainPage(db)
            if x == '3':
                managementpage.MainPage()
            if x == '4':
                userhistorypage.MainPage()
            if x == '5':
                reportpage.MainPage()
            if x == '0':
                return -1
        else:
            print("Invalid syntax, Try again:")
            takeinput()
    while True:
        print("Type the option you want to choose and press Enter [0-5]:")
        tabulate(
            "Option Service".split(),
            [
                "1 Billing".split(),
                "2 Inventory".split(),
                "3 Management".split(),
                "4,User History".split(','),
                "5 Reports".split(),
                "0 Quit".split(),
            ],
            linesbetweenrows=True,
        )

        # WriteDB(db,'STOCK.DB')
        # TODO write important

        if takeinput() == -1:
            Clear()
            break
        Clear()
