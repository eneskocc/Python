
# -*- coding: utf-8 -*-
"""
@author: enesk
"""

# Öncelikle gerekli kütüphaneleri import ediyoruz
import requests
from bs4 import BeautifulSoup as bs

giris_url='https://pusula.pau.edu.tr/'
#cerez bilgilerlini tutuyor
#kullanici ve şifreyi değiştirinin sadece
with requests.Session() as s:
    bilgiler={
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__VIEWSTATE':'/wEPDwUKLTU5MDkwNjE5MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFF2x2UHVzdWxhJGNoa0JlbmlIYXRpcmxhtEsW+fLWqqj+I4KULnPHoekofN87Hj32QXtXolJCEn8=',
        '__VIEWSTATEGENERATOR':'C2EE9ABB',
        '__EVENTVALIDATION':'/wEdAAUJTHCVtRmtVoi90F000LPtZvO7t1gssCkvoSdRSGW2avXTqPgLPMEo2kTsdSiWptGb/jwcNsYAGSQFb7fHqVGXlzVaTh9IQ1IZVv0bihklWyqYkZTRvcRsxgMg2r1bp+NJPhiQ2hBi+uROeBZqJo7n',
        'lvPusula$txtKullanici':'KULLANİCİADİ',
        'lvPusula$txtSifre':'ŞİFRE',
        'lvPusula$btnGiris':'Giriş',
        'email':''
    }

    #post işlemi ile bilgileri yolayıp giriş yapıyoruz
    giris_yap = s.post(giris_url, data=bilgiler)
    
    #girişi yapıldığını kontrol etmek için
    anasayfa=s.get('https://pusula.pau.edu.tr/Login.aspx') 
    
    #notalrın olduğu sayfa ya get işlemi yapıyoruz
    notlari=s.get('https://obis.pau.edu.tr/Grade/notgoruntuleme.aspx')
    
    #giriş yaptığımızı kontrol amaclı isimin get ettiğimşz sayfada olup olmadığını kontrol ediyoruz
    if 'İSİM SOYİSİM' in anasayfa.text:
        print('giriş yaptınız')
        soup =bs(notlari.content,"html.parser")
        notlari = soup.find(id='ctl00_ContentPlaceHolderIcerik_rgSonNotlar').find_all('tbody')
        veri=notlari[0].contents
        #dongu için
        dongu=len(veri)-1
        
        for i in range(1,dongu):
            #notlar ve ders ismi td tagleri arasında olduğu için td leri ayırıdım
            notlar=veri[i].find_all("td")
            
            #bizim bilgilerimiz 0 ile 3 elemanlar 
            ders=notlar[0].text
            notu=notlar[3].text
            
            #ve son olarak ders adini ve notu pastırıyoruz
            print(ders+"ders notu = "+notu)
            print("----------"*3)
       
    else:
        print('olmadı')
