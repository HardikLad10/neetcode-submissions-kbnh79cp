# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
We can use DFS here to check if a node and its children satisfy the given condition

If they do, we use recursive dfs to call same fn on its lst and rst
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Lets create a helper fn dfs -> for a given node, l, r 
        def dfs(node, l, r):
            # emtpy tree -> valid bst
            if not node:
                return True
            
            # Main condition
            if not (l < node.val < r):
                return False
            
            return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)

        return dfs(root, float("-inf"), float("inf"))  

            
                
        