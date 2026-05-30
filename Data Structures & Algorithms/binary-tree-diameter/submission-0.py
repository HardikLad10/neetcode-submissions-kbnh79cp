# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
from eg 1, we understand that to diam as 3, we considered both right subtree and left subtree

Thus, we first need to know the height of each subtree, then add it and update the res var.

"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # making it global so that dfs can also access

        # to calc height of tree
        def dfs(curr):
            if not curr:
                return 0
                
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right) # considering 1 for the curr node as well

        dfs(root) # Call dfs on root node
        return self.res