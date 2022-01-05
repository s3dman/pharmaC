from main import ReadDB

def Login():
    passfile = ReadDB('MANAGEMENT.DB')
    x = input("Please enter admin password: ")
    if x.strip() == Decoder(passfile['password']):
        return 0
    return -1

def Encoder(x):
    y = ''
    for i in x:
        y += str(ord(i))[::-1] + '�'
    return y[::-1]

def Decoder(x):
    x = x[::-1].split('�')
    y = ''
    for i in x[:-1]:
        y += chr(int(i[::-1]))
    return y
