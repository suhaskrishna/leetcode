class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.trie = {}
            
    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root
        
        for i in range(len(word)):
            ch = word[i]
            if not ch in temp.trie:
                temp.trie[ch] = self.TrieNode()
            
            temp = temp.trie[ch]
        
        temp.isEnd = True

    def search(self, word: str) -> bool:
        
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if not ch in node.trie:
                    if ch == ".":
                        for k in node.trie:
                            if(search_in_node(word[i+1: ], node.trie[k])):
                                return True
                    return False
                else:
                    node = node.trie[ch]
            
            return node.isEnd
                
        return search_in_node(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
print(obj.search("a"))
print(obj.search(".at"))
obj.addWord("bat")
print(obj.search(".at"))
print(obj.search("an."))
print(obj.search("a.d."))
print(obj.search("b."))
print(obj.search("a.d"))
print(obj.search("."))