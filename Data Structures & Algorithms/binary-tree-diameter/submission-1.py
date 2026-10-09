# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We have to return a val(diam) -> lets store that in a res variable
For each node, we can check the LST max height and RST max height and add them to get longest diam wrt that node.

Also, we can store a res variable globally, check self.res = max(self.res, left + right) -> This updates the curr max diam in the res

Now, for calc maxDepth from a curr node, we can define a seperate dfs(curr) fn
This fn calls itself recursively on l and r leaf nodes, updates the max diam -> max(res, l+r) and finally returns the curr max depth -> 1 + max(l,r)

This max depth will be carried to the parent to check its own depth and continue the fn 

"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Define global var 
        self.res = 0 

        def dfs(curr):
            # edge case
            if not curr:
                return 0
            
            # assume we are at root, from here we want to call the leaf nodes thru recursive dfs

            leftHeight = dfs(curr.left) # -> These recursive fns will return their resp max height
            rightHeight = dfs(curr.right)

            # after this, we will just check and update our global res
            self.res = max(self.res, leftHeight + rightHeight)

            # finally our dfs should return depth of curr
            return 1 + max(leftHeight, rightHeight)

        # Now we call dfs on root
        dfs(root)

        return self.res
        