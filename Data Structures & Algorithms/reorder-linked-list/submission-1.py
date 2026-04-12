# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # finding middle ele / portion1 and portion2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reversing portion2
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merging p1 and p2, 
        first, second = head, prev
        while second:   # Assuming portion2 always shorter
            tmp1, tmp2 = first.next, second.next
            first.next = second     #Reversing links
            second.next = tmp1      
            first, second = tmp1, tmp2            #Switching variables
            