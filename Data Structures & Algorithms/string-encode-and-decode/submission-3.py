"""
Its imperative to handle special characters from the string, so a regular seperator like ,/ wont 
work on its own

We can use # to seperate each string from list of strings, but the string itself can have a # in it.

So the best way to do encoding is: length of curr str + # + str

Decode:
Assume this encode s: "4#neet4#code"
so we need to seperate out the length of indv str, then skip first # sign and then iterate the rest of the encode s, and append the next 4 bits in the res array
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        # init local res as str
        res = ''

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # start of ptr
        # s in the encode like 4#neet4#code
        #lets dissect the 
        while i < len(s):
            # let j be the ptr till the # sign, so we know the len(indv str)
            j = i
            while s[j] != '#':
                j += 1
            
            # lets take the len of indv str and conv into int
            length = int(s[i:j]) # conv to int so that we have 4 and not '4'
            # we need to know the start and end of the indv string
            start, end = j + 1, j + 1 + length
            res.append(s[start : end]) # append to res = ['neet']
            # now we shift i to end of curr indv str
            i = end
        return res

