class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # easy way：直接按照题意依次移动
        for step in shift:
            # python的字符串中 [a:b]表示包含a不包含b
            # 左移
            if step[0] == 0:
                s = s[step[1]:] + s[0:step[1]]
            # 右移
            else:
                s = s[len(s)-step[1]:] + s[0:len(s)-step[1]]

        return s
