# https://leetcode.com/problems/implement-trie-prefix-tree/
# Recursive is faster but this was written in 15mins. Don't ask too much
class Trie:
    def __init__(self):
        self.chars = {}
        

    def insert(self, word: str) -> None:
        if not word:
            return
        ch = word[0]
        if ch not in self.chars:
            self.chars[ch] = TrieNode(ch)
        self.chars[ch].insert(word, 0)
            
        
    def search(self, word: str) -> bool:
        if not word:
            return False
        ch = word[0]
        return self.chars[ch].search(word, 0) if ch in self.chars else False
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        ch = prefix[0]
        return self.chars[ch].startsWith(prefix, 0) if ch in self.chars else False
     
        
class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.end = False
        self.down = {}
        
        
    def insert(self, word: str, idx: int) -> None:
        if idx+1 == len(word):
            self.end = True
            return
        elif word[idx+1] not in self.down:
            self.down[word[idx+1]] = TrieNode(word[idx+1])
        self.down[word[idx+1]].insert(word, idx+1)
        
        
    def search(self, word: str, idx: int) -> bool:
        if idx+1 == len(word):
            return self.end
        ch = word[idx+1]
        return False if ch not in self.down else self.down[ch].search(word, idx+1)
        
        
    def startsWith(self, prefix:str, idx: int) -> bool:
        if idx+1 == len(prefix):
            return True
        ch = prefix[idx+1]
        return False if ch not in self.down else self.down[ch].startsWith(prefix, idx+1)