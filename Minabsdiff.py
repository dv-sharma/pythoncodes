class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sortedarr=sorted(arr)
        result=[]
        absdiff=float('inf')

        left=0
        right=1

        while left<len(arr)-1:
            diff=abs(sortedarr[left]-sortedarr[right])
            print(f'diff is {diff}')
            if diff<absdiff:
                absdiff=diff
                result=[]
            if diff==absdiff:
                result.append([sortedarr[left],sortedarr[right]])
            left+=1
            right+=1
        return result

        

        
