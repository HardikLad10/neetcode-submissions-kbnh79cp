# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
We will do this using slow and fast ptrs
Logic is -> for each itr, slow moves linearly, fast moves 2xslow
So if a cycle exist, we can find that using if fast == slow -> return true
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        
        return False