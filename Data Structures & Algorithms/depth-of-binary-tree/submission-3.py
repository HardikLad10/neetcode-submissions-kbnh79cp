# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
What is depth? -> well for root its 1, then for each level of children, it increases

Thus, we can calc depth of l & r subtree separately
And for the problems sake, depth = 1(root) + Max(maxDepth(LST), maxDepth(RST))

The above condition is the entire logic of this problem, 
we can use iterative dfs here, to calc maxDepth of l and r subtree
Since depth will be default 1 -> for any Treenode
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # recursive DFS for indv subtree depth calc, then comparison
        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return depth