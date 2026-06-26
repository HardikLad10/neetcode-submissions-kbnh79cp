"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Deep copy -> For each node, create a new copy, and create a copy of its neighbors as well

Since we already know the structure of Node, and how neighbors are stored,
We first init a hashmap(dict)
Then we create copy of curr node(store in hashmap k,v = node, copy)
Then run a for loop for each of curr nodes neighbors, 
then append dfs(nei) in copy.neighbors which is a list in the node class

"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            # base condt, if copy is already created, return the copy
            if node in oldToNew:
                return oldToNew[node]
            
            # create copy of curr node
            copy = Node(node.val)
            # append said copy to our HashMap
            oldToNew[node] = copy

            # run a for loop for each neighbor of curr node
            for nei in node.neighbors:
                # append said neighbors as neighbors of copy. neighbors is a list
                copy.neighbors.append(dfs(nei))

            return copy # in the original fn call this copy will be returned

        return dfs(node)