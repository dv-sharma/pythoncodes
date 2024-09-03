class Solution:
    def reverseWords(self, s: str) -> str:

        wordlist=s.split(' ')
        finallist=[]
        

        for words in wordlist:
            finallist.append(words[::-1])
        
        ans=' '.join(finallist)
        return ans
