import mysql.connector
mydb = mysql.connector.connect(host = '10.10.1.121', user= 'kuba', passwd = 'kalipso2')

mycursor = mydb.cursor()
mycursor.execute('show databases')

for i in mycursor:
    print(i)
    
mycursor.execute('use student')
mycursor.execute('select * from student')

my_result = mycursor.fetchall()


import numpy as np
import pandas as pd

import os






# =============================================================================
#                   something differernt
# =============================================================================
dire = '/home/kuba/Data'
os.chdir(dire)

df = pd.read_csv('avocado.csv')
df.to_csv('avocadoo.csv',index = False)


lista = [1,2,3,4,5]
lista[::-1]


