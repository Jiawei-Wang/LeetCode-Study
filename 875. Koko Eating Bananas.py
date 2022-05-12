# https://leetcode.com/problems/koko-eating-bananas/discuss/152506/Binary-Search-Java-Python-with-Explanations
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = 1, max(piles)
        
        while lo <= hi:
            K = lo + ((hi - lo) >> 1)
            if self.countTimeEatAllAtSpeed(K, piles) <= H:  # count time to eat all bananas at speed K
                hi = K - 1
            else:
                lo = K + 1
        return lo
    
    def countTimeEatAllAtSpeed(self, K, piles):
        countHours = 0  # hours take to eat all bananas
        
        for pile in piles:
            countHours += pile // K
            if pile % K != 0:
                countHours += 1
        return countHours


# 05-11-2022
# https://leetcode.com/problems/koko-eating-bananas/discuss/769702/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 对题意的理解：找到尽可能小的k，使得sum(math.ceil(piles[i]//k)) = h
        # 解题思路：在已知上下限的情况下使用二分法查找
        
        # 检查当前k是否合格
        def feasible(speed) -> bool:
            # return sum(math.ceil(pile / speed) for pile in piles) <= h  # slower        
            return sum((pile - 1) // speed + 1 for pile in piles) <= h  # faster

        
        left, right = 1, max(piles)
        while left < right: 
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid # 这里不能使用 mid-1，因为在mid是可能解的情况下，mid-1未必是
            else:
                left = mid + 1 # 如果mid不是符合要求的解，那么k必定至少是mid+1
        return left
        """
        对while loop为什么不用 <= 的理解：
        假设上一轮mid=5符合要求，且left=4，那么right=5
        本轮left=4，right=5，mid=4，假设不符合要求（此时我们知道答案为mid=5）
        那么下一轮left=5，right=5，如果有 <= ，就会无止尽地循环下去
        """
