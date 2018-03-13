from urllib.request import urlopen                 
import json, urllib.request                      
url = input("Enter the url: \n")                   
resp = urllib.request.urlopen(url)                 
data = json.loads(resp.read().decode())          
invest = set([])                                 
try:
    for i in range(1,len(data)+1):
        for x in data['Episode '+str(i)]:
            l = x['investors'].replace('and',',')      
            l=l.split(',')                             
            for i in range(len(l)):
                l[i] = l[i].strip('\n').lstrip().rstrip()   
            invest = invest.union(l)
    invest.remove('')
    oo = {e:[] for e in invest}                       
    for i in range(1,len(data)+1):
        for x in data['Episode '+str(i)]:
            sample = x['investors']
            for i in oo:
                if i in sample:
                    oo[i].append(x['product'].lstrip().rstrip().strip('\n'))      
    for k in sorted(oo, key=lambda k: len(oo[k]), reverse=True):              
        print(str(k)+" : "+str(oo[k]))                                 
        print("\n")
except(ValueError, KeyError, TypeError):
    print("Error in JSON format")
