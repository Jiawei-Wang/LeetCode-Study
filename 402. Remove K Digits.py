class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 一次遍历，将每个元素都放进去，如果找到更好的，就把它丢弃
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)

        # join: 将括号内元素使用''给连接起来
        # lstrip: 将点号前的变量，所有从左侧开始包含括号内元素的部分去除，比如这里就是把左侧的string中开头的0全部去掉
        return ''.join(out[:-k or None]).lstrip('0') or '0'
