"""
Contrast to the 2Sum problem, here the target is 0, and we need to return vals and not indices

No duplicate triplets in given, so no 0,0,0 
nums may contain more than 1 triplet


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
           #0
        n = len(nums) # no of vals
        result = [] # -> this may have many list of nums
        # now we check our curr num and call the helper fn to find sum -(curr num)
        for i in range(n - 2):
            # let go off +ve nums since we wont find any pair beyond this
            if nums[i] > 0:
                break
            # handle duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #helper call
            # pass args of nums array, curr + 1, and -(curr num)
            for pair in self.twoSum(nums, i + 1, -nums[i]):
                result.append([nums[i]] + pair)
            
        return result
            


        # Lets define a helper fn which returns a pair of num where sum == target   
    def twoSum(self, nums, start, target):
            pair = [] # this fn return a pair of num list

            l, r = start, len(nums) - 1
            # run main while loop
            while l < r:
                # Calc curr total
                total = nums[l] + nums[r]
                # condts for total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                # else will mainly have the happy flow
                else:
                    pair.append([nums[l], nums[r]])
                    l += 1 # shift l to look for next pair, if exist
                    # we skip the repeated num for curr + 1 pos
                    while l < r and nums[l] == nums [l - 1]:
                        l += 1
            return pair
                    







