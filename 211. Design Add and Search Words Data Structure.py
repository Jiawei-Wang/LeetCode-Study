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