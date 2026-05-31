# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    We can calc height using DFS. 
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True, 0] # [issubTreebalanced, height]

            left, right = dfs(root.left), dfs(root.right)
            
            # now check if the entire tree is balanced or np. Check diff <=1 as well
            balanced = (left[0] and right[0] and 
                            abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]