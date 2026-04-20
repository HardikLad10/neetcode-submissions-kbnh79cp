# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0  # to increment upto nth smallest
        stack = [] # init empty stack set
        curr = root # manages curr node
        while curr or stack:
            while curr:  # runs while curr not null
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop() # pops the smallest and curr gets that val
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
