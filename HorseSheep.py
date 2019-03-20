# -*- coding: utf-8 -*-
"""


@author: enesk
"""
import random
class Game():
    def __init__(self,horse,sheep):
        self.horse=horse
        self.sheep=sheep
    def Horse(self):
        x=random.randint(1,10)
        if x<=3:
            self.horse=self.horse+3
        elif x<=7:
            if self.horse<1:
                self.horse=0
            else:
                self.horse=self.horse-1
        else:
            self.horse=self.horse+1
        return self.horse
    def Sheep(self):
        y=random.randint(1,10)
        if y<=2:
            self.sheep=self.sheep+4
        elif y<=4:
            if self.sheep<2:
                self.sheep=0
            else:
                self.sheep=self.sheep-2
        elif y<=8:
            self.sheep=self.sheep+2
        else:
            self.sheep=self.sheep+1
        return self.sheep
def show(x):
    a=" "
    for i in range(x):
        a=a+"- "
    a=a+"* "
    for i in range(19-x):
        a=a+"- "
    return a
        
horsePoint=0
sheepPoint=0        
while True:
    game=Game(horsePoint,sheepPoint)
    sheepPoint=game.Sheep()
    horsePoint=game.Horse()
    if horsePoint>=20:
        print("                  the horse won!!!"+str(horsePoint))
        break
    elif sheepPoint>=20:
        print("                  the sheep won!!!"+str(sheepPoint))
        break
    print("Horse |"+show(horsePoint)+"| Point =  "+str(horsePoint))
    print("Sheep |"+show(sheepPoint)+"| Point =  "+str(sheepPoint)+"\n")
    
    
    
        
