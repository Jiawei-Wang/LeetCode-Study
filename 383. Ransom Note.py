class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 两个collections.Counter(list)相减得到的是每个剩余的元素和它剩余个数的dictionary
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
