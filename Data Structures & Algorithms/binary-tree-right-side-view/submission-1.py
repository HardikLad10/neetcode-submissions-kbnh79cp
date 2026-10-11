# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Given root = [1,2,3,null,4,null,5] -> return only the right side view/ nodes visible from right side, i.e. res = [1,3,5]

Quite logical to use BFS here -> appen right leaf node values, ignore or discard left leafnodes?
One critical edge case here is that if the rst is empty, all the RIGHT MOST NODES -> append to result



"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = collections.deque()
        
        q.append(root)

        while q:
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightSide is not None:
                res.append(rightSide.val)
        
        return res