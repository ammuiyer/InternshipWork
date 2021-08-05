import pandas
import numpy
import math
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/meenakshiiyer/Internship/SVa5snZ5f6.csv')
print(df)

#print(df.iloc[4,4])
top_downs = []
for x in range(len(df['host'])) :
    str = df.iloc[x-1,4]
    top_downs.append(df.iloc[x-1, 1])
    if ".com" in str :
        i = str.index('.') +1
        j = len(str) - 4
        str2 = str[i: j:]
        df.at[x-1, 'host'] = str2
        #print(str2)
    else :
        continue

print(df)


for i in range(1, len(top_downs)):
  
        key = top_downs[i]
        j = i-1
        while j >=0 and key > top_downs[j] :
                top_downs[j+1] = top_downs[j]
                j -= 1
        top_downs[j+1] = key

#print(top_downs)

#sorts the df by download using built in fuction 
df = df.sort_values(by=['sdnb'], ascending=False)
print("DF Sorted by Download")
print(df)
print("Top 5")
print(df.head())

#sorts the df by upload using built in fuction 
df = df.sort_values(by=['sunb'], ascending=False)
print("DF Sorted by Upload")
print(df)
print("Top 5")
print(df.head())

#sorts the df by time using built in fuction 
df = df.sort_values(by=['elapse'], ascending=False)
print("DF Sorted by Time")
print(df)
print("Top 5")
print(df.head())