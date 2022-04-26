class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1: sorted(string): 
        # time nlogn, space: n (2 new strings)
        # return sorted(s) == sorted(t)
        # there is another method for list: list.sort(): same time, 1 space (no new list)
        
        # solution 2: dictionary: time n, space: n
        # dic1, dic2 = {}, {} # 学习这个初始化dict的语法
        # for item in s:
        #     dic1[item] = dic1.get(item, 0) + 1 # 学习这个初始化key value pair的语法
        # for item in t:
        #     dic2[item] = dic2.get(item, 0) + 1
        # return dic1 == dic2
        
        # solution 3: improve upon 2, use list:
        # dic1, dic2 = [0]*26, [0]*26 # 1.节约空间，2.直接初始化
        # for item in s:
        #     dic1[ord(item)-ord('a')] += 1 # 每个字母对应的位置是其与a的unicode差值
        # for item in t:
        #     dic2[ord(item)-ord('a')] += 1
        # return dic1 == dic2
        
        # solution 4: 1 list:
        dic = [0]*26
        for i in s:
            dic[ord(i)-ord('a')] += 1
        for i in t:
            dic[ord(i)-ord('a')] -= 1
            
        for i in dic:
            if i != 0:
                return False
        return True