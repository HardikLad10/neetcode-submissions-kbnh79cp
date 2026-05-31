# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
we need to store res, where maxSum is stored
Simultaneously, in the dfs function, each node will return max path sum without split
our dfs will also compute max path sum with split

Along the way, we need to consider 0 when we return the max path from a node, since node.val can be -ve as well. Tf, max(maxPathSum, 0)

"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # return maxPathSum w/o splitting
        def dfs(root):
            if not root: 
                return 0

            # calc left and right Max using recursive DFS
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # handle -ve vals
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # calc maxPathSum in res using splits
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return only maxpathsum w/o splitting
            return root.val + max(leftMax, rightMax)

        dfs(root)  

        return res[0]

