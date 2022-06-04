# sliding window
# time n (for loop) * n (check list)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        1. 检查s2中每个和s1长度相同的substring（time n)
        2. 第一次时创建一个长度为26的list并populate
        3. 以后向前步进时只需要更新list即可（time n)
        any(): 有任意一个元素为True则返回True，否则返回False, time O(n)
        """
        l1 = len(s1)
        l2 = len(s2)
        if l2 < l1:
            return False
        
        # target is the counter for all chars in s1
        target = [0] * 26
        for char in s1:
            target[ord(char)-ord('a')] += 1
        for char in s2[0:l1]:
            target[ord(char)-ord('a')] -= 1
        if not any(target):
            return True
        
        for i in range(l1, l2):
            target[ord(s2[i-l1])-ord('a')] += 1
            target[ord(s2[i])-ord('a')] -= 1
            if not any(target):
                return True
        return False
# 疑问：对于上面的答案，是否有O(1)检查list是否全部为0的方法？
# 答案：并没有，但是使用counter和defaultdict会缩短运行时间


# sliding window but with counter
# time n^2
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1, d2 = Counter(s1), Counter(s2[:len(s1)])
        for start in range(len(s1), len(s2)):
            if d1 == d2: return True # compare two counters: O(n)
            d2[s2[start]] += 1
            d2[s2[start-len(s1)]] -= 1
            if d2[s2[start-len(s1)]] == 0:
                del d2[s2[start-len(s1)]]
        return d1 == d2


# sliding window but with defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ctr1 = collections.defaultdict(int)
        ctr2 = collections.defaultdict(int)
        for x in s1: 
            ctr1[x] += 1
        for x in s2[:len(s1)]: 
            ctr2[x] += 1
            
        i = 0; j = len(s1)
        
        while j < len(s2):
            if ctr2 == ctr1: 
                return True
            
            ctr2[s2[i]] -= 1
            if ctr2[s2[i]] < 1: 
                ctr2.pop(s2[i]); # 删除元素来尽量缩短dict
            ctr2[s2[j]] = ctr2.get(s2[j], 0) + 1
            i += 1
            j += 1
            
        return ctr2 == ctr1