def commonelementlist(list1,list2):
	
    listfinal=list1+list2
    listreturn=[]
    listdict={}
    for words in listfinal:
          if words in listdict:
                listdict[words]+=1
          else:
                listdict[words]=1
    
    for key,values in listdict.items():
          if values>1:
                listreturn.append(key)
    return listreturn
                
          
          

	


if  __name__=='__main__':
	list1=[1,3,4,8,9]
	list2=[2,4,1,8,5,9]
	
	print(commonelementlist(list1,list2))
	   