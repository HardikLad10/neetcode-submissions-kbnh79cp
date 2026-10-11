# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
From the constraints, we see that 0 < k <= no of nodes in the tree -> thus k exists always(hence tree also exists)

We can use BST in order traversal here to find the smallest ele first -> in order: left > node > right

So, if we constantly shift to left subtree to find the smallest, we will then need to visit the most recent ancestor.
Thus, by this logic -> we need a DS where we can pop most recent val added to it -> Stack!

So we just go from node.left -> add that to stack

How to check if a node is the smallest? -> check if node.right exist(or curr not null, i.e. left does not exist anymore), if not -> we found our smallest. We will keep a count of this and either update our k(given) or maintain a var n(for doing n==k)

We repeat this until the stack is empty or curr.node not null/none
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      # Init a stack for ancestory
      stack = []
      curr = root # for 1st itr -> start from root

      # run a main while loop until either of stack is empty of curr not null
      while curr or stack:
        # Condt to find smallest
        while curr:
            stack.append(curr) # ancestor added to stack
            curr = curr.left # shift curr ptr
        
        # visit the next node by going l -> most recent ancestor
        curr = stack.pop()
        k -= 1

        if k==0:
            return curr.val

        # Edge case -> check right subtree l -> node -> RST
        curr = curr.right
      return -1
