# -*- coding: utf-8 -*-
"""
@author: enesk
"""

import requests
from bs4 import BeautifulSoup

url='https://tureng.com/tr/turkce-ingilizce/'

word=input("kelime giriniz = ")

r=requests.get(url+word)

soup=BeautifulSoup(r.content,'html.parser')

gelen=soup.find_all("table",{"id":"englishResultsTable"})

veri=gelen[0].contents

for i in range(3,len(veri),2):
    
    ing=veri[i].find_all("td",{"class":"tr ts"})
    
    if len(ing)==1:
        
        print(ing[0].text)
    
