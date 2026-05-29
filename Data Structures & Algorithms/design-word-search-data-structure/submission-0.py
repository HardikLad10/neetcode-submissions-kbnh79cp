class TrieNode:
    def __init__(self):
        self.children = {} # eg a: TrieNode
        self.word = False # to check if endOfWord

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root # initially curr var is root val(placeholder)

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() # in the dict -> c : TrieNode()
            # shift ptr
            cur = cur.children[c]
        cur.word = True # this indicated endOfWord

    def search(self, word: str) -> bool:
        def dfs(j, root):
            # init cur as root placeholder
            cur = root 

            for i in range(j, len(word)): 
                c = word[i]

                if c == '.':
                    # check for all children of cur c, ie. all vals in dict
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)
        