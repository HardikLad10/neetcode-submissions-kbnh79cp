class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0 # window -> starts at 0, 0 resp

        # continue till our right ptr overflows
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest

            res += 1
        
        return res