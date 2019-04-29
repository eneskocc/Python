# -*- coding: utf-8 -*-
"""

@author: enesk
"""

sayilar=[10,5,9,-1,7,2,25,75,1]

for j in range((len(sayilar))):
    for i in range(0,(len(sayilar)-1)):
        temp=sayilar[i]
        if temp>sayilar[i+1]:
            sayilar[i]=sayilar[i+1]
            sayilar[i+1]=temp
            
for i in range(len(sayilar)):
    print(sayilar[i])