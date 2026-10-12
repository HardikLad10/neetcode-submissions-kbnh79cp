class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Init hashset
        hashset = set() 
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
            
        
      

        