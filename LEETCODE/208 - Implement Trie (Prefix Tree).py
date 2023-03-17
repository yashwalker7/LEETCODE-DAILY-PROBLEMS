class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        n = self
        for c in word:
            idx = ord(c) - ord('a')
            if n.children[idx] is None:
                n.children[idx] = Trie()
            n = n.children[idx]
        n.is_end = True

    def search(self, word: str) -> bool:
        n = self._search_prefix(word)
        return n is not None and n.is_end

    def startsWith(self, prefix: str) -> bool:
        n = self._search_prefix(prefix)
        return n is not None

    def _search_prefix(self, prefix: str):
        n = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if n.children[idx] is None:
                return None
            n = n.children[idx]
        return n


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
