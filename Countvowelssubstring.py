import re
class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        vowels=set('aeiou')
        n=len(word)
        left=0
        count=0

        while left<n:
            if word[left] in vowels:
                seen=set()

                for right in range(left,n):
                    if word[right] in vowels:
                        seen.add(word[right])
                        if len(seen)==5:
                            count+=1
                    else:
                        break
            
            left+=1
        return count
