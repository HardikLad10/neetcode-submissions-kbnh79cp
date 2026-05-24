class TrieNode:
    def __init__(self):

        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # init cur ptr
        cur = self.root

        # iterate word with a for loop and check if exists in children
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # shift cur ptr
            cur = cur.children[c]
        
        # now that we have inserted the word, and iterated the word, we establish EOW
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        # Iterate word to check if whole exists in Trie also check endOfWord
        for c in word:        
            # edge case
            if c not in cur.children:
                return False
            # shift cur ptr
            cur = cur.children[c] #?

        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        # similar to search, but we dont wont the entire word

        for c in prefix:
            if c not in cur.children:
                return False
            # shift cur ptr
            cur = cur.children[c]
        return True

        