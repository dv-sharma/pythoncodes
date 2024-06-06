def missingnumber(list1):
    
    sumfull=0
    N=list1[-1]
    sumfull=N*(N+1)//2

    nummissing=sumfull-sum(list1)
    print(nummissing)

""" XOR METHOD NEEDED"""

    







if __name__=="__main__":
    list1=[1,2,3,5]
    missingnumber(list1)
