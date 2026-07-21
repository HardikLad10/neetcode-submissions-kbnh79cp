"""
Imperative to visualize that we rather want to find no of disjoint pairs. This makes it easy
If all the nodes are connected, then basically we just have one connected component. 


So in our hashmap, we will have {node: [adj nodes]}
we maintain a visited set.
first run dfs through nodes in hashmap(graph)
Check return condt, 
further we add node to visited -> hence we should not consider said node again
Then run for loop in adj nodes
Run recursive dfs on adj nodes, same process

init a cnt var
Finally run for loop on range(n) i.e. on graph/ hashmap -> to make sure all disjoint nodes are considered
Inside, if a node not in visited:
run dfs(node)
one dfs() call from the loop = one component found

No crazy edge cases here, since n >=1, same for edges, so the for loop on hashmap takes care of this.

return cnt

"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        # form hashMap
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            # main idea is to add node to visited, and traverse complete component in one dfs call
            # no fail condition, so just return if node already traversed
            if node in visited:
                return
            visited.add(node)

            for adj in graph[node]:
                dfs(adj)
        
        count = 0

        for node in range(n):
            if node not in visited:
                dfs(node)
                # one component processed
                count += 1
        
        return count
