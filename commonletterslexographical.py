"""Input : 
string1 : geeks
string2 : forgeeks
Output : eegks
Explanation: The letters that are common between 
the two strings are e(2 times), g(1 time), k(1 time) and 
s(1 time).
Hence the lexicographical output is "eegks"

Input : 
string1 : hhhhhello
string2 : gfghhmh
Output : hhh """

from collections import Counter
def commonstring(str1,str2):
    dict1=Counter(str1)
    dict2=Counter(str2)

    #print(dict1)

    commonset=(dict1 & dict2)

    if len(commonset) == 0: 
        print (-1) 
        return
    
    commonlist=list(commonset.elements())
    sortedcommonlist=sorted(commonlist)

    
    print ("".join(sortedcommonlist))

    






if __name__== "__main__":
    str1 = 'geeks'
    str2 = 'forgeeks'
    commonstring(str1,str2)
