# 所有char，如果是偶数个则全部加入，如果是奇数个则-1后加入，最后如果有剩的元素，随便加入一个
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1
        
        odd_number = 0
        for i in d:
            if not d[i] % 2:
                ans += d[i]
            else:
                if not odd_number:
                    ans += d[i]
                    odd_number = 1
                else:
                    ans += d[i] -1
        
        return ans


class Solution:
    def longestPalindrome(self, s: str) -> int:
        #获得每个字母的出现次数
        #对于偶数次的字母，直接加上
        #对于奇数次的字母，每个去掉一次
        #如果存在奇数次的字母，最后答案再加一
        
        #所以反推过来，答案的长度为：
        #原本长度 - 1 * 奇数次字母的总数 + 1 （如果奇数次字母存在）
        
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
    
    """
    integer & 1: 检查是否integer为奇数
    bool(): 检查是否为0
    """