# -*- coding: utf-8 -*-
"""


@author: enesk
"""

sayilar=[10,4,9,-1,7,2,21,75,1]

for i in range((len(sayilar)-1)):
    kucuk=i
    for j in range(i,(len(sayilar))):
        
        if sayilar[j]<sayilar[kucuk]:
            kucuk=j
            
    temp=sayilar[i]
    sayilar[i]=sayilar[kucuk]
    sayilar[kucuk]=temp          
        
for i in range(len(sayilar)):
    print(sayilar[i])