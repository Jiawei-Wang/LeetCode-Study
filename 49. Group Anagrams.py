class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 拿到题目第一想法：遍历每个元素，如果没有相同的就放进新的list，如果有相同的就放在对应list里
        ans = []
        dictionary = []
        for word in strs:
            if sorted(word) in dictionary:
                ans[dictionary.index(sorted(word))].append(word)
            else:
                dictionary.append(sorted(word))
                ans.append([])
                ans[dictionary.index(sorted(word))].append(word)

        return ans
# Time: 5%
# Space: 30%
