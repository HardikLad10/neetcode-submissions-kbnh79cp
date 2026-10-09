# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
At curr node -> if height of |lst - rst| > 1, return False
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(curr):
            if not curr:
                return 0 # -> this is the height if no leaf node exist
            
            # Check on each depth -> lst and rst
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)

            if abs(leftHeight - rightHeight) > 1:
                self.balanced = False
            
            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.balanced

