"""
s, t = "z","z"

ret => true

s = racecar, t = carrace
seen = {}
for i in s: 

    seen.append[i, 1]

for i in t:
    if i in   
    s = "x", t = "x" => 
    s  = "axe", t = "axx" => 
    s = "racecar", t = "carrace"

    carrace
    racecar  
        """

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Lets maintain 2 hashmaps for count
        countS, countT = {}, {}

        for i in range(len(s)):
            #update count
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)


        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

