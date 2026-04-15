# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q: # Main while loop, traverses for all levels
            qlen = len(q) # curr length of q
            level = [] # interior sublist of levels
            for i in range(qlen):
                node = q.popleft() # pops the left most val in q 
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)

        return res
