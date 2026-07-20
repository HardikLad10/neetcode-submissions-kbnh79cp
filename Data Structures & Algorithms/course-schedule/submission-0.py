"""
Cycles!


We maintain a visited set to check if curr node(crs or preq) in visited. If yes, we detect cycle and return False

We create a hashmap preMap -> {crs: [preq]}

Then for our dfs(crs) -> we check if crs in visited, if preMap[crs] is empty,
then add crs to visited,
trace all preq of that crs, check cycles while tracing
Then backtrack and reset preMap[crs] == []

Then finally we run a for loop for range(numCourses) to check of all the crs, to make sure
disjoint graphs are taken care off


"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to preq list

        preMap = {i: [] for i in range(numCourses)}

        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        # create empty visited set
        visited = set()

        # init main dfs fn
        def dfs(crs):
            # check first if crs exists in visited set
            if crs in visited:
                return False
            # check if preq of curr crs is empty
            if preMap[crs] == []:
                return True     # no preq, so skip 
            
            # now if both condt dont satisfy, add crs to visited
            visited.add(crs)

            # run recursive dfs on all preq
            for preq in preMap[crs]:
                if not dfs(preq):
                    return False # if cycle found while tracing all preq
            
            #backtrack condt
            visited.remove(crs)
            # now we will reset preMap[crs]
            preMap[crs] = []

            return True

        

        # now check for all crs in prequisites

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        
        return True
