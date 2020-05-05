class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 暴力解：
        for i in s:
            if i not in s[s.index(i)+1:]:
                return s.index(i)
        return -1

        # O(n)：
        # 两重遍历，第一遍建立dictionary，第二遍找到第一个value为1的元素，输出其下标
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
