
import re
def frequencycount(str1):
    
    worlistnew= re.sub(r'[^a-zA-Z0-9\s]', '', str1)
    print(worlistnew)
    wordlist=worlistnew.split()
    print(wordlist)

    d={}
    
    for word in wordlist:
        if word not in d:
            d[word]=0
        d[word]+=1
    print(d)





if __name__== "__main__":
    str1=" My name is Divyam , My full name is Divyam Sharma."
    frequencycount(str1)
