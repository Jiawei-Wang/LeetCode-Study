"""
逻辑：用一个trie来代替现有的words list，然后在board 2d list上dfs来寻找符合条件的words中的元素
"""

# trienode有两个method，一是创建一个node，另一个是创建整个trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, node, word):
            # node: 当前在trie上的位置
            # word：当前dfs已经找到的prefix（比如words中有一个'apple'，而此时在board上dfs已经找到'a','p','p'）
            
            # 每次走到新的位置时先检查
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or # 如果越界
                board[r][c] not in node.children or (r, c) in visit): # 如果当前元素不是我们想要的，或者已经被遍历过
                return
            
            # 确定这个位置：1.不越界，2.未被遍历过，3.元素是想要的
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord: # 之前创建trie时已经确定此位置是words中某个元素的结尾
                res.add(word) 
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        # first build a trie with every word in words
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
            
        # 对于board上每个位置，都假设其可能为某个words中元素的起始位置，使用dfs寻找
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "") # 起始位置均为root（dummy node），且此时无任何已有元素
        
        return list(res)
        