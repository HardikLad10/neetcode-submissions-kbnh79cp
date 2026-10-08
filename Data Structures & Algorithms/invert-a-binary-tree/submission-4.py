# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Basically we need to swap the l and r subtrees wrt the node

Lets start from the Root -> we will do a swap using temp var here
temp = l
l = r
r = temp

Now one pair is inverted, we can do the same with the rest of the 2 subtrees in the same way

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case:
        if not root: return None

        #swap children
        temp = root.left
        root.left = root.right
        root.right = temp

        # Now we use recursion to do the same with l and r subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
