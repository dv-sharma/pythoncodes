def stringcompressor(str1):

    left=0
    right=0
    count=1
    resultstr=''
    while right<len(str1):
        right+=1
        if right<len(str1) and str1[left]==str1[right]:
            count+=1
        else:
            if count>3:
                resultstr+=str(count)+'x'+str1[left]
            else:
                resultstr+=str1[left:right]
            left=right
            count=1
    
    return resultstr
        


if __name__=='__main__':
    str1='aabcaaaade'
    str2='aabcccaaaddddde'
    print(stringcompressor(str2))