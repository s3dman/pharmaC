from os import system, name
from pprint import pprint
import datetime
def Clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

tax = "12"

db = {
    'I001': ['Paracetamol', {'9-2021':10, '12-2021':21, '3-2022':20}, 375],
    'I002': ['Captropil', {'9-2021':10, '12-2021':21, '3-2022':25}, 475],
    'I003': ['Ciplatin', {'9-2021':10, '12-2021':21, '3-2022':30}, 500],
    'I004': ['Heparin', {'9-2021':10, '12-2021':21, '3-2022':35}, 700],
    'I005': ['Quinine', {'9-2021':10, '12-2021':21, '3-2022':40}, 210],
    'I006': ['Mecillinam', {'9-2021':10, '12-2021':21, '3-2022':45}, 70],
    'I007': ['Marinol', {'9-2021':10, '12-2021':21, '3-2022':50}, 100],
    'I008': ['Penicillin', {'9-2021':10, '12-2021':21, '3-2022':55}, 400],
    'I009': ['Digoxin', {'9-2021':10, '12-2021':21, '3-2022':60}, 350],
    'I010': ['Vinblastine', {'9-2021':10, '12-2021':21, '3-2022':65}, 600],
}
finalbill =  [
    ['I007', 'Marinol', 100, {'12-2021': 21, '3-2022': 50, '9-2021': 10}, 8100],
    ['I001', 'Paracetamol',375,  {'12-2021': 21, '3-2022': 20, '9-2021': 10},  19125],
    ['I010', 'Vinblastine',  600,  {'12-2021': 21, '3-2022': 65, '9-2021': 10},  57600],
    ['I005', 'Quinine', 210, {'12-2021': 21}, 14910],
    [99735, 1196820]
]
x = ['SNo', 'ID', 'Item', 'Expiry', 'Quantity', 'Rate', 'Net Price']
y = []
for i in finalbill[:-1]:
    temp = list(i[3].items())
    y.append([finalbill.index(i)+1,i[0],i[1],temp[0][0],temp[0][1],"Rs "+str(i[2]),"Rs "+str(i[-1])])
    for i in temp[1:]:
        y.append(["","","",i[0],i[1],"",""])
    y.append(["","","","","","",""])
tabulate(x,y,"Neville Joseph Sabu",finalbill[-1],prependspace=9)
