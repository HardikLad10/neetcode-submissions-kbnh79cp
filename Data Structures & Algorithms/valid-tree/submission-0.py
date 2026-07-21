"""
edges make a valid tree if there exist no cycles for the given edges

TF, we need to detect cycle here(similar to course schedule prob) -> one diff, the edges are undirected
i.e. if edges are [0,1], then in our hashmap,
0:[1]
1:[0]

we will maintain a visit set and check if curr node exists in this set, if it does -> cycle exist and we 
return false
for our dfs, we pass i and prev -> since the edges are undirected, we also check that i and prev dont make a cycle


"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False

        adj = {i: [] for i in range(n)}

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue # false cycle, where prev is basically parent node in tree
                # now run recursive dfs on adj, pass curr i as prev in this dfs call
                if not dfs(j, i):
                    return False # checking cycle for adjacent nodes
            return True


        return dfs(0, -1) and n == len(visit)