# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # check edge cases
        if not lists or len(lists) == 0:
            return None

        #merge each pair of k LLs in lists until last 1 remains
        while len(lists) > 1:
            mergedLists = [] #temp var for storing reduced k LLs per round

            for i in range(0, len(lists), 2): 
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeLL(l1,l2))
            lists = mergedLists # store final LL in lists
        
        return lists[0] # basically return head

    
    def mergeLL(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next # head of merged LL