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


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:

            # 和 list() 类似，将一个字符串变成每个字符组成的一个tuple
            key = tuple(sorted(word))

            # 返回当前key的value（一个list），如果不存在，返回 []，并加上[word]
            dictionary[key] = dictionary.get(key, []) + [word]

        return list(dictionary.values())
# Time: 72%
# Space: 30%
