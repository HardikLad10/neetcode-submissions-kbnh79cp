"""
temperatures  = [70, 72, 71, 69, 70, 74, 76]
res = [1, 4, 3, 2, 1, 1, 0]

We can use a stack that stores only the indicies from temperatures
We will be running loop on temperatures:

We do this check- > if curr temp > temperatures[stack[-1]] and stack:
prev = stack.pop()
res[i] = i - prev

stack.append(i)

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]] :
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        
        return res