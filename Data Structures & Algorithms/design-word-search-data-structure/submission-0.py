class Trie:
    def __init__(self):
        self.word = False
        self.bache = {}

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.bache:
                curr.bache[c] = Trie()
            curr = curr.bache[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.bache.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.bache:
                        return False
                    cur = cur.bache[c]
            return cur.word

        return dfs(0, self.root)
