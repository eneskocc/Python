# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:12:22 2019

@author: enesk
"""

import random
secim=" "
player=0
computer=0
def menu():
    print("taş   = 1\nkağıt = 2\nmakas = 3\nSeciminiz?")
   
while True:
    menu()
    pc = random.choice(["1", "2", "3"])
    secim=input("")
    #oyuncudan bir girdi alınıyor
    if secim=="1" or secim=="2" or secim=="3":
        print("-------------------")
    else:
        print("1,2 veya 3 seciniz!!")
        menu()
    #oyunun devam etme durumunu kontrol ediyor
    if player>10:
        print("Bu oyunu Player kazandı..\n Puanı = "+str(player))
        break
    elif computer>10:
        print("Bu oyunu Computerr kazandı..\n Puanı = "+str(computer))
        break
    #elin kazananı kontrol edip puan artırıyor
    if secim==pc:
        print("Bu elde berabere kaldınız..")
        print("-------------------")
        player=player+1
        computer=computer+1
    elif (secim=="1" and pc=="3") or (secim=="2" and pc=="1") or (secim=="3" and pc=="2"):
        print("Bu elde Player kazandı..")
        print("-------------------")
        player+=2
    else:
        print("Bu elde Computer kazandı..")
        print("-------------------")
        computer+=2
        
        


