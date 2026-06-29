class Trie:
    def __init__(self):
        self.word = False
        self.bache = {}

class PrefixTree:

    def __init__(self):
        self.root = Trie()
        

    def insert(self, word: str) -> None:
        curr = self.root
        # print(curr)
        for c in word:
            if c not in curr.bache:
                curr.bache[c] = Trie()
            curr = curr.bache[c]
        curr.word = True



    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.bache:
                return False
            curr = curr.bache[c]
        return curr.word
        
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.bache:
                return False
            curr = curr.bache[c]
        return True
        
        