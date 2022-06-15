# BFS：每次向邻居走一步，如果在遍历完所有word前走到endWord则返回当前步数
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:                 
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            
            # 找到邻居并加入queue中
            for i in range(len(word)):
                # 将当前的word的所有变体找出来
                for c in range(ord('a'), ord('z')+1):
                    next_word = word[:i] + chr(c) + word[i+1:]
                    # 如果变体在list中则加入queue中作为邻居
                    if next_word in wordList:
                        wordList.remove(next_word) 
                        # 上面这行这样写有两个好处：
                        # 1.不需要再额外使用一个visited set
                        # 2.只保留到达此node的最短路径（能2步到没必要3步到）
                        queue.append([next_word, length + 1])
        return 0
                        
                        
    """
    可以把题目转换为：找到从起始node到目标node的最短路径
    其中路径weight均为1，但adj list的关系被隐藏（即我们无法直接获得当前遍历的word的邻居）
    找邻居的传统思路：遍历list，其中每个word都拿出来和当前的word逐个char对比，如果两者刚好相差一个char则视为邻居
    找邻居的新思路：将当前word的所有（只改变一个char）的变体找出来，查看是否在list中
    """