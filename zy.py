#########################################################
First Unique Character ina String

from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:

        mapdict=defaultdict(int)

        for values in s:
            mapdict[values]+=1
        
        for i,vals in enumerate(s):
            if mapdict[vals]==1:
                return i
        
        return -1
        
######################################################################################
SECOND WAY
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map: character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
############################################################################################################

SECOND UNIQUE CHARACTER IN A STRING
from collections import defaultdict

class Solution:
    def secondUniqChar(self, s: str) -> int:
        # Step 1: Create a dictionary to count occurrences of each character
        mapdict = defaultdict(int)

        # Step 2: Count each character's occurrences in the string
        for values in s:
            mapdict[values] += 1

        # Step 3: Identify the unique characters in the order they appear
        unique_chars = []
        for i, vals in enumerate(s):
            if mapdict[vals] == 1:
                unique_chars.append(i)

        # Step 4: Return the index of the second unique character if it exists
        if len(unique_chars) >= 2:
            return unique_chars[1]
        else:
            return -1

# Example usage
solution = Solution()
print(solution.secondUniqChar("leetcode"))  # Output: 0
print(solution.secondUniqChar("loveleetcode"))  # Output: 2
print(solution.secondUniqChar("aabb"))  # Output: -1
####################################################################################################################################


MOVE ZEROES
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
  
        for i in range(len(nums)):

            if nums[i] == 0 and nums[i] < nums[i+1] :

                nums[i] , nums[i+1] = nums[i+1], nums[i]
            else : 
                continue
#################################################################################################################################
VALID ANAGRAM
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if the lengths of the strings are not equal
        if len(s) != len(t):
            return False
        
        # Use Counter to count characters in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Compare the two Counter objects
        return count_s == count_t

# Test case
s = "aacc"
t = "ccac"
sol = Solution()
print(sol.isAnagram(s, t))  # Output should be False
##########################################################################################################
GROUP ANAGRAM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for word in strs:
            count=[0]*26
            for i in word:
                count[ord(i)-ord("a")]+=1
            result[tuple(count)].append(word)
        return result.values()
####################################################################################################################


REVERSE LINKED LIST
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev= None

        curr=head

        while curr:

            next=curr.next
            curr.next=prev

            prev=curr
            curr=next
        return prev


########################################################################################################

LINKED LIST MEET
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_set=set()
        curr=headA
        
        while curr:
            first_set.add(curr)
            curr=curr.next
        
        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr=curr.next

        return None
      ############################################################


REVERSE BINARY TREE
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp=root.left
        root.left=root.right
        root.right=tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        
        
