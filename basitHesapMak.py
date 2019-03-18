def topla(a,b):
    return a+b
def cikar(a,b):
    return a-b
def carp(a,b):
    return a*b
def bol(a,b):
    return a/b
def menu():
    print("işlem seciniz\ntoplama = +\ncıkarma = -\ncarpma  = *\nbolme   = /")
    girdi=input("")
    if girdi=="+" or girdi=="-" or girdi=="*" or girdi=="/":
        sayi1=int(input("birinci sayiyi giriniz  = "))
        sayi2=int(input("ikinci sayiyi giriniz   = "))
        print("")
        if girdi=="+":
            print("işlem sonucunuz = "+str(topla(sayi1,sayi2)))
        elif girdi=="-":
            print("işlem sonucunuz = "+str(cikar(sayi1,sayi2)))
        elif girdi=="*":
            print("işlem sonucunuz = "+str(carp(sayi1,sayi2)))
        else:
            print("işlem sonucunuz = "+str(bol(sayi1,sayi2)))
        answer=input("devam etmek istiyor musunuz = (n/N)")
        if answer=="n" or answer=="N":
            menu()
        else:
            print("teşekkür ederiz")
    else:
        print("lütfen aşağıdakilerden birini seciniz")
        menu()
menu()
