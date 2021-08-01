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
downld = df_ip['TotalDownload']
upld = df_ip['TotalUpload']

# convert to mega bytes
temp = []
temp2 = []
for x in range(5):
    temp.append((downld.iloc[x-1])/8000000)
    temp2.append((upld.iloc[x-1])/8000000)

downld = temp
upld = temp2
tim = df_ip['TotalTime']

for x in range(1) : 
    data = [downld, upld]
    X  = numpy.arange(5)
    fig = plt.figure()
    plt.plot()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)

    plt.xticks(X, ip_list)
    plt.xlabel("Ips")
    plt.ylabel("Bits")
    plt.title("Each Ip Download and Upload")
    plt.show() 
downld = df_hosts['TotalDownload']
upld = df_hosts['TotalUpload']
tim = df_hosts['TotalTime']


top_downs = []
top_downs2 = []
top_ups = []
top_time = []
top_hosts = []
top_ups2 = []
top_time2 = []

for x in range(len(download)) :
    top_downs.append(download[x])
    top_ups.append(upload[x])
    top_time.append(time[x])
    top_downs2.append(download[x])
    top_ups2.append(upload[x])
    top_time2.append(time[x])
    



for i in range(1, len(top_downs)):
  
        key = top_downs[i]
        j = i-1
        while j >=0 and key < top_downs[j] :
                top_downs[j+1] = top_downs[j]
                j -= 1
        top_downs[j+1] = key


for x in range(5) :
    top_hosts.append(host[top_downs2.index(top_downs[x-1])])

apps = (top_hosts[0], top_hosts[1], top_hosts[2], top_hosts[3], top_hosts[4])
y_pos = numpy.arange(len(apps))
height = [top_downs[0],top_downs[1],top_downs[2],top_downs[3],top_downs[4]]

plt.bar(y_pos, height, align='center', alpha=0.5)
plt.xticks(y_pos, apps)
plt.title('Top Download' )
plt.xlabel('Apps')
plt.ylabel('Values (MB)')

plt.show()

for i in range(1, len(top_ups)):
  
        key = top_ups[i]
        j = i-1
        while j >=0 and key < top_ups[j] :
                top_ups[j+1] = top_ups[j]
                j -= 1
        top_ups[j+1] = key

for x in range(5) :
    top_hosts.append(host[top_ups2.index(top_ups[x-1])])

apps = (top_hosts[0], top_hosts[1], top_hosts[2], top_hosts[3], top_hosts[4])
y_pos = numpy.arange(len(apps))
height = [top_ups[0],top_ups[1],top_ups[2],top_ups[3],top_ups[4]]

plt.bar(y_pos, height, align='center', alpha=0.5)
plt.xticks(y_pos, apps)
plt.title('Top Upload' )
plt.xlabel('Apps')
plt.ylabel('Values (MB)')

plt.show()

for i in range(1, len(top_time)):
  
        key = top_time[i]
        j = i-1
        while j >=0 and key < top_time[j] :
                top_time[j+1] = top_time[j]
                j -= 1
        top_time[j+1] = key
  

for x in range(5) :
    top_hosts.append(host[top_time2.index(top_time[x-1])])

apps = (top_hosts[0], top_hosts[1], top_hosts[2], top_hosts[3], top_hosts[4])
y_pos = numpy.arange(len(apps))
height = [top_time[0],top_time[1],top_time[2],top_time[3],top_time[4]]

plt.bar(y_pos, height, align='center', alpha=0.5)
plt.xticks(y_pos, apps)
plt.title('Top Time Usage' )
plt.xlabel('Apps')
plt.ylabel('Minutes')

plt.show()