# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Give a btree root = [1,2,3,4,5,6,7] -> we need to return a LOL res = [[1],[2,3],[4,5,6,7]]
Thus we want to append each level in the res as a list

So on a highlevel, we can maintain a queue, and keep adding the nodes first, when a level is done, we can 
pop from that queue, and add that level in a list and append that to res

Check len(q) -> to determine how many nodes to pop and add to the currList, ie. curr level

Do this until our queue is empty?
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # main List
        res = []
        q = collections.deque() # init queue
        q.append(root) # only append the root node for now
        
        # Main high level loop to check all the nodes
        while q:
            currList = [] # currList for the current Level
            
            # now we run a for loop on len(q), i.e. for the current level
            for i in range(len(q)):
                node = q.popleft()
                currList.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if currList:
                res.append(currList)
        
        return res
        



