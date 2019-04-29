# -*- coding: utf-8 -*-
"""

@author: enesk
"""

sayilar=[10,4,9,-1,7,2,21,75,1]

for i in range(1,len(sayilar)):
 
    deger = sayilar[i]
        
    j = i-1
    while j >=0 and deger< sayilar[j] :
        sayilar[j+1] = sayilar[j]
        j -= 1
    sayilar[j+1] = deger
        
for i in range(len(sayilar)):
    print(sayilar[i])
        