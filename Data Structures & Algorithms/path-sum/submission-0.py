# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Given a BST, return true if a path sum equates to target -> False if otherwise

As we iterate thru the BST -> we can update the target -> target - node.val

Start from the root, upcate the target, then we need to use recursive dfs to check target in both LST and RST -> so our pathSum return statement should have an OR
and the recursive fn call have values as root.left/root.right and updated target
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        # Your code goes here
        if not root:
            return False

        # return True if target is found
        if not root.left and not root.right:
            return target == root.val
        target -= root.val

        """this final return will call dfs recursively and check for solution in both   LST and RST without repetition(whichever comes first)"""
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)
        
        