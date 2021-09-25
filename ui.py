from main import *
import time
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

Prepend = ' '*8

def LoadingScreen():
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

    HomePage()

def HomePage():
    print("Type the option you want to choose and press Enter:")
    tabulate(
        "Option Service".split(),
        [
            "1 Billing".split(),
            "2 Inventory".split(),
            "3 Management".split(),
            "0 Quit".split(),
        ],
        linesbetweenrows=True,
    )
    def takeinput():
        x = input("❯ ")
        if x in "1 2 3 0".split():
            if x == '1':
                # BillingPage()
                pass
            if x == '2':
                # InventoryPage()
                pass
            if x == '3':
                # ManagementPage()
                pass
            if x == '0':
                return
        else:
            print("Invalid syntax, Try again:")
            takeinput()
    takeinput()
LoadingScreen()
