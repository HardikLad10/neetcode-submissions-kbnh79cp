"""
exactly one solution exists

1 idx array

Given that nums sorted in non d'ing order, and we cannot use additional space
These clues point that we should not be using hash here
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init 2 ptrs
        first, last = 0, len(numbers) - 1 

        while last > first:
            currSum = numbers[first] + numbers[last]
            if currSum == target:
                return [first + 1, last + 1]
            if currSum < target:
                first +=1
            else:
                last -=1
        
        return []