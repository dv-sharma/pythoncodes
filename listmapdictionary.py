
def convertdict(list1,list2):
    finaldict={}
    
    for i in range(len(list1)):
        finaldict[list1[i]]=list2[i]


    print(finaldict)

def converttuple(dict1):
    for keys,values in dict1.items():
        print((keys,values))
        

if __name__== "__main__":
    list1=["Naina","Kim","Kylie"]
    list2=[1,12,123]
    dict1={'Naina': 1, 'Kim': 12, 'Kylie': 123}
    convertdict(list1,list2)
    converttuple(dict1)