from main import ReadDB
from getpass import getpass

# prompt password for login and check with decrypted password obtained from MANAGEMENT.DB
def Login():
    passfile = ReadDB('MANAGEMENT.DB')
    x = getpass()
    if x.strip() == Decoder(passfile['password']):
        return 0
    return -1

# function to hash/encode password
def Encoder(x):
    y = ''
    for i in x:
        y += str(ord(i))[::-1] + '�'
    return y[::-1]

# function to unhash/decode password
def Decoder(x):
    x = x[::-1].split('�')
    y = ''
    for i in x[:-1]:
        y += chr(int(i[::-1]))
    return y
