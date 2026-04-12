

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping character count(key) too the list of anagrams(val)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1. # if a has ascii val 80 ord(a) - ord("a") = 0

            res[tuple(count)].append(s)

        return list(res.values())