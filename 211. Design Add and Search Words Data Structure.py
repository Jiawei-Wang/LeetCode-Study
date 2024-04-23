class TrieNode:
    def __init__(self):
        self.children = {} # a: TrieNode
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:
        def dfs(index, root):
            cur = root

            for i in range(index, len(word)):
                c = word[i]
                if c == ".": # 如果遇到 '.' 则对所有child node进行遍历
                    for child in cur.children.values():
                        if dfs(i + 1, child): # 只要有一个成功即算成功
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# 2024
from collections import defaultdict
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.children[char]
        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(pivot, node):
            current = node
            for i in range(pivot, len(word)):
                char = word[i]
                if char == ".":
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
            return current.is_end

        return dfs(0, self.root)

"""
understanding: compare to 208. Implement Trie
1. if there is no dot, just do the same as 208
2. if there is dot: we do a dfs everytime a new dot shows up
3. in dfs: instead of searching one node, we need to search all possible nodes
4. two things are needed: node, and next char in input string
"""