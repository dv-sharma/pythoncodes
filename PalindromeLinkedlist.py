# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast=head
        slow=head
            # find middle
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        previous=None
        while slow:
            tmp=slow.next
            slow.next=previous
            previous=slow
            slow=tmp
        # check palindrome
        left,right=head,previous
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        
        return True


        



        
