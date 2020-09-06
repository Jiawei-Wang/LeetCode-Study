# 读题想法：一次遍历，每找到一个 ？，将它置换为与前面和后面都不同的一个char
# 如果第一个char是 ？，则只需要和第二个char不同即可，如果是最后一个，则只需要和倒数第二个不同即可

# 解法1: 1.只使用3个字符即可;2.很巧妙的解决了第一个和最后一个元素的问题
class Solution:
    def modifyString(self, s: str) -> str:
        # res是需要返回的答案,初始化为空string
        res = ""
        # prev是遍历时的指针,初始化为'?'
        prev = '?'
        # 遍历s
        for i, c in enumerate(s):
            # next就是当前元素的下一个元素,如果当前元素是末尾,则它的下一个元素可以视为'?'
            next = s[i + 1] if i + 1 < len(s) else '?'
            # 当前元素的处理:
            # a.difference(b) 将set a中set b没有的元素返回(也可以使用 a - b的形式)
            # set.pop()随机获得一个元素(也可以用于将set中唯一的元素返回)
            prev = c if c != '?' else set({'a', 'b', 'c'}-{prev, next}).pop()
            res += prev
        return res
