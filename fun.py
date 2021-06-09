dict1={}
string=str(input("Enter String="))
i=0
j=0

def most_frequent(string):
    for i in range(0,len(string)):
        count=0
        for j in range(0,len(string)):
            if(string[i]==string[j]):
                count=count+1
        if string[i] not in dict1.keys():
            dict1.update({string[i]:count})
    res={key:val for key, val in sorted(dict1.items(),key=lambda ele:ele[1],reverse=True)}
    keys=list(res.keys())
    val=list(res.values())
    for i in range(0,len(dict1)):
        print(str(keys[i])+"="+str(val[i]))
            
most_frequent(string)
