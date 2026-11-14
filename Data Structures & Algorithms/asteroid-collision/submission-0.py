"""
We need to take in acc the foll examples:
[2,-4], [-2,4]: IN the first case, the 2nd asteroid will collide, but for the case2, they are moving apart

Thus we can store surviving asteroids in a set, since we need to check the most recent asteroid and its 
dir, we can store them in a stack

so if stack(-1) is -4 and curr val is 2 -> no collision
but if stack(-1) is 4 and curr val is -2 -> collision -> 2nd is smaller thus 1st survives

Lets take all positions for ref: [2,4,-4,-1]
For this eg, we will append the first in stack, then for the next, since no collision, append in stack
for -1, since stack(-1) is 2, there will be a collision, we keep the bigger num

"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # logic for collision
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    # both a and last ele is same
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)

        return stack