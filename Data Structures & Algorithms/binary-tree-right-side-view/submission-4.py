# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Given root = [1,2,3,null,4,null,5] -> return only the right side view/ nodes visible from right side, i.e. res = [1,3,5]

Quite logical to use BFS here -> 
Maintain a res array and and append treenodes into a queue. Since the 1st node is always added to res, we append that to queue

We then run a while loop until queue is empty:
Use a rightMost var(none initially), 
Run a main for loop(len(q)) -> this is for each level
We make sure that the rightMost var will always have the rightmost node
i.e. For a level, we traverse through all nodes in level, and always swap last node in that level to rightMost
This gives us what we want, and we also make sure not to miss edge cases

One critical edge case here is that if the rst is empty, all the RIGHT MOST NODES -> append to result

Then append rightMost to Res

Finally return res

"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        # Init a deque and add the root of Tree to deque
        q = deque([root])

        #Run an outer while loop until the deque is empty
        while q:
            #init a rightMost var -> this stores the currRightmost var for a level
            # rightMost must swap as we traverse through the level
            rightMost = None # init it to none
            
            # nowe we run a for loop for BFS/ level order traversal
            for i in range(len(q)):
                node = q.popleft() # -> This pops curr node from the currLevel

                #We update rightMost -> if the node is not null
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)

            # Now we append rightMost for curr level to res
            if rightMost:
                res.append(rightMost.val)

        return res

