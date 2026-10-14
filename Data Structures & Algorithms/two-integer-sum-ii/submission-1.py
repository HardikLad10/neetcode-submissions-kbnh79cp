"""
exactly one solution exists

1 idx array

Given that nums sorted in non d'ing order, and we cannot use additional space
These clues point that we should not be using hash here
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init 2 ptrs
        l, r = 0, len(numbers) - 1 

        while r > l:
            # check currSum
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l + 1, r + 1] # happy flow
            # init inc dec logic and also edge case
            if currSum < target:
                l +=1
            else:
                r -=1
        
        return []