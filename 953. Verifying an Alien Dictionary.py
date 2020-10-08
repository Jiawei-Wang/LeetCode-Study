class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 将order中每个char和它的index，保存在m这个dictionary中
        m = {c: i for i, c in enumerate(order)}

        # words是一个2d list，每个row记录的是words中一个单词的所有字符在order中的值
        words = [[m[c] for c in w] for w in words]

        # all(): check if every element is true
        # zip(): 将括号内所有（在这里是两个）元素各自的每个元素配对在一起，这里的意思是把words里每个元素和
        # 它后面的那个元素配对在一起
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
