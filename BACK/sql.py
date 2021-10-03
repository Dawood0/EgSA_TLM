# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:01:56 2021

@author: MShar
"""

import mysql.connector

mydb = mysql.connector.connect(
   # host="153.92.220.1",
   host="sql514.main-hosting.eu",
   user="u952728553_egsa",
   password="Egsa1234",
   database="u952728553_egsa"
)

print("CONNECTED SUCESSFULLY")

# Sample code

# mycursor = mydb.cursor()

# sql = "SELECT * FROM main WHERE name = "+gov

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)