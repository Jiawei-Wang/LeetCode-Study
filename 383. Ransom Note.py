# 检查是否可以用magazine中的元素来组成ransomNote，每个元素只能使用最多一次
# 等同于检查ransomNote是否是magazine的子集
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 暴力解：ransomNote中的元素挨个检查是否在magazine中：time n^2 space 1
        
        
        # 先用magazine创建dict，time n, space n
        d = dict()
        for char in magazine:
            d[char] = d.get(char,0)+1
        
        for i in ransomNote:
            if i not in d or d[i] <= 0:
                return False
            d[i] -= 1
        
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 两个collections.Counter(list)相减得到的是每个剩余的元素和它剩余个数的dictionary
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
