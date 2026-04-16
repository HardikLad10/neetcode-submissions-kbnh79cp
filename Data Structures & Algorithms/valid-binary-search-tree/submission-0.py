# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # helper fn to check BST validation
        def isValid(node, left, right):
            if not node:
                return True  # executed for leaf node child ie. after full traversal returns true
    
            if  not (left < node.val and right > node.val):
                return False  # executes when BST breaks

            return (isValid(node.left, left, node.val) and 
                    isValid(node.right, node.val, right)) 
            
        return isValid(root, float("-inf"), float("inf"))
            