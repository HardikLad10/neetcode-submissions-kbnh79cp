"""
Return any correct order of completing courses, and empty list if its not possible to complete all the courses.


Similar to course Schedule I, we will have a visited set to detect cycle(cycle for avoiding confusion)

There are 3 states of a node:
visited, visiting and unvisited
We maintain 2 sets -> cycle and visit and an output array
Now, we want to append a node(course) to output, if the node does not have any further preq

remove crs from cycle as a backtracking condt, add the same crs to visit set(to avoid tracing it again) and
finally append the course to the output list.

"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        # map -> crs:[preq] in the hashMap
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        output = []
        visit, cycle = set(), set()

        # init main dfs fn
        def dfs(crs):
            # if cycle detected return false
            if crs in cycle:
                return False
            if crs in visit:
                return True # already visited, so skip this 
            
            # if both condt not met, move to next logic
            cycle.add(crs)
            for preq in preMap[crs]:
                if not dfs(preq):
                    return False # if we find cycle while tracing all preq
            
            # backtracking condt
            cycle.remove(crs)
            # add crs to visit, hence avoid retracing the same path
            visit.add(crs)
            output.append(crs)

            return True

        # check for all the prequisites, ie all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return [] # empty list if cycle found 

        return output









