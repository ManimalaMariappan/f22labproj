//CODE FOR THE TEST PROJECT BY F22 LABS//

from urllib.request import urlopen                 //Module to retreive data from url
import json, urllib.request                        //Module to parse json data
url = input("Enter the url: \n")                   //getting url through input function and storing in a variable
resp = urllib.request.urlopen(url)                 //open the url through urlopen
data = json.loads(resp.read().decode())            //Decoding the json data
invest = set([])                                   //creating an empty set
try:
    for i in range(1,len(data)+1):
        for x in data['Episode '+str(i)]:
            l = x['investors'].replace('and',',')      //Replacing 'and' by comma in the investors names
            l=l.split(',')                             //splitting the names individually which contains comma
            for i in range(len(l)):
                l[i] = l[i].strip('\n').lstrip().rstrip()   //Removing left and right side spaces and '\n' in the data
            invest = invest.union(l)
    invest.remove('')
    oo = {e:[] for e in invest}                       //Creating array
    for i in range(1,len(data)+1):
        for x in data['Episode '+str(i)]:
            sample = x['investors']
            for i in oo:
                if i in sample:
                    oo[i].append(x['product'].lstrip().rstrip().strip('\n'))      //Adding investors names with products  
    for k in sorted(oo, key=lambda k: len(oo[k]), reverse=True):              //Sorting the array using its length
        print(str(k)+" : "+str(oo[k]))                                       //Printing the array
        print("\n")
except(ValueError, KeyError, TypeError):
    print("Error in JSON format")
