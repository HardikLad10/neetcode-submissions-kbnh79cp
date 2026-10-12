# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
We need good visualization to understand this
For an optimal solution, the goal is to reverse the given LL -> in one pass
So as we iterate thru the LL, we change the pointer, update the next, and then move ahead

By default, we can have a curr, and a prev ptr... prev followed by curr always
Initially , prev is None, and curr is at head

in the main while loop, that runs until curr is None:
Using the nxt ref, and switching curr.nxt to prev, followed by shifting prev and curr -> we get to completing one loop

We continue this till end of our LL -> i.e. while curr is None, 
so here, the last ele whould be prev. Prev is our new head for the reversed ll, so we return prev here
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            # init a next ptr, which is always a next reference to curr
            nxt = curr.next
            # Now that we have a next ref, we can change direction
            curr.next = prev
            # Now its time to shift prev
            prev = curr
            
            # now finally, we shift our curr to what we have in nxt ref
            curr = nxt
        
        return prev