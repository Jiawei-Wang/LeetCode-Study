# 思考：验证一个substring是否可以通过倍增还原string，要比从string中找到符合条件的substring要容易
# 答案最长为str2，最短为0，所以可以以str2本身为起点，每次找到一个可以整除的正整数（范围从1一直到len(str2))，然后验证此正整数对应的substring是否可被两个string都整除
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        
        def canDivide(string, str_len, substring, substr_len):
            for i in range(0, str_len-substr_len+1, substr_len):
                if substring != string[i:i+substr_len]:
                    return False
            return True
            
        # i 代表str2被整除的次数，比如i = 3即将str2分为三等分
        # i最小1，最大len(str2)，如果所有循环都没找到符合条件的substring则返回空string
        # 如果一个substring可以整除str2，那么它必然是从0到某个位置
        for i in range(1, l2+1): 
            if (l2 % i == 0) and (l1 % (l2//i) == 0): # 首先str2长度必须是i的倍数，且str1长度必须是此substring的倍数
                cur_str = str2[0:l2//i] # 找到此时的substring然后验证可否用它整除str1和str2
                if canDivide(str1, l1, cur_str, l2//i) and canDivide(str2,l2, cur_str,l2//i):
                    return cur_str
        return ''