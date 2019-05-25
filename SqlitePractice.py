
"""
Created on Sat Mar 23 02:07:49 2019

@author: enesk
"""

import sqlite3
class sqle:
    def __init__(self,FirstName,LastName,city,email):
         self.FirstName=FirstName
         self.LastName=LastName
         self.city=city
         self.email=email
        
    #Dışardan gelen firstname göre silme fonksiyonu
    def deleteCostemer(self):
         sql='Delete from customers where FirstName=?'
         connection = sqlite3.connect("chi.db")
         connection.execute(sql,(self.FirstName,))
         connection.commit()
         connection.close()
            
    #Dışardan gelen firstName göre güncelleme fonksiyonu
    def updateCustomer(self):
        sql='update customers set City=? where FirstName=?'
        connection = sqlite3.connect("chi.db")
        connection.execute(sql,(self.city,self.FirstName,))
        connection.commit()
        connection.close()
        
    #Dışardan gelen girdiler ile ekleme fonksiyonu
    def insertCustomer(self):
        connection = sqlite3.connect("chi.db")
        sql='insert into customers (firstName,lastName,city,email) values(?,?,?,?)'
        connection.execute(sql,(self.FirstName,self.LastName,self.city,self.email,))
        connection.commit()
        connection.close()
        
    #Gelen girdiye göre arama yapıp firstname ile lastname bastıran fonksiyon
    def selectCustomer(self):
        connection = sqlite3.connect("chi.db")
        sql='select FirstName,LastName from customers where FirstName like ?'
        cursor = connection.execute(sql,(self.FirstName,))

        for row in cursor:
            print("First Name = "+row[0])
            print("Last Name = "+row[1])
            print("*********")

        connection.close()

def menu():
    i=input("Select = (S/s)\ninsert = (I/i)\nupdate = (U/u)\ndelete = (D/d)\nFinish = (F/f)")
    return i

def inputs():
    a=[]
    a.append(input("FirstName = "))
    a.append(input("LastName = "))
    a.append(input("City = "))
    a.append(input("Email = "))
    return a

while True:
    a=menu()
    if a=="S" or a=="s":
        s=inputs()
        sql=sqle(s[0],s[1],s[2],s[3])
        sql.selectCustomer()
        
    elif a=="I" or a=="i":
        s=inputs()
        sql=sqle(s[0],s[1],s[2],s[3])
        sql.insertCustomer()

    elif a=="U" or a=="u":
        s=inputs()
        sql=sqle(s[0],s[1],s[2],s[3])
        sql.updateCustomer()

    elif a=="D" or a=="d":
        s=inputs()
        sql=sqle(s[0],s[1],s[2],s[3])
        sql.deleteCostemer()

    elif a=="F" or a=="f":
        print("Finish")
        break
    else:
        print("please enter correctly!!!")
        menu()
