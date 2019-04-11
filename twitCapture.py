# -*- coding: utf-8 -*-
"""
@author: enesk
"""
# Öncelikle gerekli kütüphaneleri import ediyoruz
import requests
from bs4 import BeautifulSoup

url ="https://twitter.com/ens172"

r=requests.get(url)

soup =BeautifulSoup(r.content,"html.parser")
# ol tagi alıyoruz class ismi belirtip
gelen=soup.find_all("ol",{"class":"stream-items js-navigable-stream"})
# gelen veriyi parcalıyoruz
veri=gelen[0].contents
# 1 den başladığı ve birer ara ile twitleri için bu şekilde bir for döngüsüne soktum
for i in range(1,len(veri),2):
    # zaman smal tagleri içinde tutulduğu için onları aldım
    time=veri[i].find_all("small",{"class":"time"})
    #zamanı texte cevirdim çünkü html tagleri içinde verdi bize
    saat=time[0].text
    #verinin güzel durması için reoplace ile \n leri cıkardım
    saat=saat.replace("\n","")
    #twitlerin hangi div tagi içinde olduğuna bakıp find_all cektim
    twit=veri[i].find_all("div",{"class":"js-tweet-text-container"})
    
    verii=twit[0].text
    #ve son olarak zaman ile twitleri pastırdım
    print(saat+verii)
