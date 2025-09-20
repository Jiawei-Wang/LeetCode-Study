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


# 再次回顾题目：
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # 拿到题第一想法：遍历每个元素，让其再遍历每个已知list，如果它不符合所有list，让其单独成为一个list
        
#         if not strs:
#              return [[""]]
        
#         # space: n
#         sort = []
#         ans = []
        
#         # time: n^2logn
#         for i in strs: # n
#             cur = sorted(i) # nlogn
#             if cur not in sort: # n
#                 sort.append(cur)
#                 ans.append([i])
#             else:
#                 ans[sort.index(cur)].append(i)
#         return ans

        # 和上一解逻辑相同，每个元素sort后找到对应位置并加入，使用dict更加易读
        # ans = {}
        # for w in strs:
        #     key = tuple(sorted(w))
        #     ans[key] = ans.get(key, []) + [w] # list + list = list，所以这里是创建空list，然后不断延长
        # return list(ans.values()) # 使用dict.values()来获取所有value
        
        # 使用第242题：valid anagram来进一步优化，主要集中在sorted()上：
        # hmap = collections.defaultdict(list) # 使用defaultdict也是一种初始化dict的手段
        # for st in strs:
        #     array = [0] * 26
        #     for l in st:
        #         array[ord(l) - ord('a')] += 1 # array记录的是st中26个字母每个字母的出现次数
        #     hmap[tuple(array)].append(st)
        # return hmap.values()


# O(n*mlogm)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for string in strs: # O(n)
            key = str(sorted(string)) # O(mlogm)
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
        return list(hashmap.values())


# array is not hashable but tuple is
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            freq = [0] * 26   
            for c in word:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)   # tuples are hashable
            groups[key].append(word)

        return list(groups.values())