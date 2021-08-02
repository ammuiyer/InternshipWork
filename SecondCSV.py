import pandas
import numpy
import math
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/meenakshiiyer/Internship/SVa5snZ5f6.csv')
print(df)

#print(df.iloc[4,4])
for x in range(len(df['host'])) :
    str = df.iloc[x-1,4]
    if ".com" in str :
        i = str.index('.') +1
        j = len(str) - 4
        str2 = str[i: j:]
        df.at[x-1, 'host'] = str2
    else :
        continue

print(df)