from urllib.request import *
from json import load

ip=input('Enter IP address: ')
url='https://ipinfo.io/'+ip+'/json'

res=urlopen(url)
#print(type(res))
#print(res)

data=load(res)
#print(type(data))
#print(data)
for x in data.keys():
    print(x,':',data[x])