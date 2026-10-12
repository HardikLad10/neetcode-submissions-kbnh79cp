# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Thinking of the brute force -> we can check using 2 lists, if the reverse of l2 == l1 -> return true. But this takes O(n) space

An optimal way is -> combine fast and slow ptr logic with the reverse LL logic

- We can get the mid using slow and fst ptr

Then using curr, prev = mid, None -> we can use the reverse LL logic to reverse 2nd half of LL

- The last block will check if values are same
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Slow and fast ptr logic to check mid
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Now we reverse 2nd half of the LL
        curr, prev = slow, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Now we have 2 halves, and head points to first and prev points to last
        l, r = head, prev

        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        
        return True



        