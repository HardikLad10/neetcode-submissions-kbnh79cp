class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if len not same, no possibility of being anagram
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # s and t will have same len, so we can iterate through any 1 
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True