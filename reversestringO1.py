class Solution:
    def reverseString(self, s: List[str]) -> None:

        
        right=len(s)-1
        left=0

        while left<=right:
            tmp=s[left]
            s[left]=s[right]
            s[right]=tmp
            left+=1
            right-=1
        print(s)

            
        """
        Do not return anything, modify s in-place instead.
        """
        
