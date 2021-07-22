import pandas
import numpy
import math
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/meenakshiiyer/Internship/SQL_report_4.csv')
#print(df)

ip = df['clientIp']
download = df['Download']
upload = df['Upload']
time = df['TimeUsage']
host = df['hostName']
row = len(ip)
BigArray = []
count = 0
#print('test')
#sorting into each client
for col in range(row-1) :

    if ip[col]!=ip[col+1]:
        count = count + 1

    
for x in range(count+1) :
    newArray = []
    BigArray.append(newArray)   
    #print(BigArray)
    
count = 0  
ip_list = [] 

for col in range(row-1) :
    BigArray[count].append(download[col])
    #print(BigArray[count])
    if ip[col]!=ip[col+1]:
        ip_list.append(ip[col])
        count = count+1

#print(ip_list)   
#print(BigArray[0])  
df_ip = pandas.DataFrame(columns=['TotalDownload', 'TotalUpload', 'TotalTime'], index=ip_list)
#print(df_ip)
total_download = 0
total_upload = 0
total_time = 0
count = 0
for col in range(row-1) :
    total_download = total_download + download[col]
    total_upload = total_upload + upload[col]
    total_time = total_time + time[col]


    if ip[col]!=ip[col+1] :
        df_ip.iat[count,0] = total_download
        df_ip.iat[count,1] = total_upload
        df_ip.iat[count,2] = total_time
        total_download = 0
        total_upload = 0
        total_time = 0
        count = count+1
print(df_ip)
#print(df)

hostNames = []
#print(host)
for col in range(len(host)):
    print(host[col])
    if (host[col] in hostNames) :
        count = 0
    else : 
        hostNames.append(host[col])

#print(hostNames)

df_hosts = pandas.DataFrame(columns=['TotalDownload', 'TotalUpload', 'TotalTime'], index=hostNames)

def is_nan(x):
    return (x != x)

for col in range(len(host)) :
    for x in range(len(hostNames)) :
        if(host[col]==hostNames[x]) :
            if(is_nan(df_hosts.iloc[x,0])) : 
                df_hosts.iat[x,0] = download[col] 
                df_hosts.iat[x,1] = upload[col]
                df_hosts.iat[x,2] = time[col]
            else :
                df_hosts.iat[x,0] = download[col] + df_hosts.iloc[x,0]
                df_hosts.iat[x,1] = upload[col] + df_hosts.iloc[x,1]
                df_hosts.iat[x,2] = time[col] + df_hosts.iloc[x,2]
            
print(df_hosts)
