"""
is array is already in asc order, we can shrink the array to find target
For this we can use binary search -> find mid = l + r //2
[1, 2, 3, 4]
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # check mid with target

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1