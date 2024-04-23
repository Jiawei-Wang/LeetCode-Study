"""
understanding：
1. Instead of for each word in words, we go through the board 
    1) which is time consuming (example: words = [abcd, abcde, abcdef])
2. we build words into trie
    2) then go through board
        2> go into dfs: only go one loop deeper when the path is in trie
3. both solutions go through the board but second one contains very limited number of dfs
"""

# TrieNode 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    # we need an extra method for Trie building
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children: # if we don't use defaultdict, we will need to check key first 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, node, prefix):
            # r, c: current location on board
            # node: current location on trie
            # prefix：当前dfs已经找到的prefix（比如words中有一个'apple'，而此时在board上dfs已经找到'a','p','p'）
            
            # 每次走到新的位置时先检查
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or # 如果越界
                board[r][c] not in node.children or # 如果当前元素不是我们想要的
                (r, c) in visited): # 如果当前元素已经被遍历过
                return
            
            # 确定这个位置：1.不越界，2.未被遍历过，3.元素是想要的且未被遍历
            # go one step forward
            visited.add((r, c)) # prevent re-visit
            node = node.children[board[r][c]] # go down the trie
            prefix += board[r][c] # append to answer string

            if node.isWord: # 之前创建trie时已经确定此位置是words中某个元素的结尾
                answer.add(prefix) # append to answer array
            
            # go down the dfs on board
            dfs(r + 1, c, node, prefix)
            dfs(r - 1, c, node, prefix)
            dfs(r, c + 1, node, prefix)
            dfs(r, c - 1, node, prefix)

            # we finish all paths through this element, we remove this element, and it can be used for other words again
            visited.remove((r, c))
        
        # first build a trie with every word in words
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        # then go through the board
        # instead of picking word from words and check the whole board
        # we check the whole board, assume every element can be a possible starting point, and dfs this element
        ROWS, COLS = len(board), len(board[0])
        answer = set()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "") # 起始位置均为root（dummy node），且此时无任何char in prefix
        
        return list(answer)
        