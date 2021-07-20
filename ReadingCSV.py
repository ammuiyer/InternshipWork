import pandas

import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/meenakshiiyer/Internship/SQL_report_4.csv')
#print(df)

ip = df['clientIp']
download = df['Download']
row = len(ip)
BigArray = []
count = 0
#sorting into each client
for col in range(row-1) :

    if ip[col]!=ip[col+1]:
        count = count + 1

    
for x in range(count+1) :
    newArray = []
    BigArray.append(newArray)   
    print(BigArray)
    
count = 0   
for col in range(row-1) :
    BigArray[count].append(download[col])
    print(BigArray[count])
    if ip[col]!=ip[col+1]:
       count = count+1
   
   
 


