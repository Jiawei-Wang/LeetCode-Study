# pick at most k elements from n elements such that 
# target = sum(speed of all elements) * min(efficiency of all elements) is maximum
# return target % (10^9+7)

# thoughts:
# if we have this:
# e = [5, 5, 5, 4, 3, 3, 2]
# s = [5, 4, 3, 3, 8, 7, 100]
# 1. [2, 100] will decrease min(efficiency of all elements)
#    but will increase sum(speed of all elements)
#    how do we know if [2, 100] should be picked or not if we use greedy on list e
# 2. how do we know if current target with <k elements is already the maximum
#    and we should stop adding new ones


# Solution 1: binary insert 
# time n^2
# first: sorting: nlogn
# second: go through each element and insert (n * n)
# space n
# logic:
# still use this as example
# e = [5, 5, 5, 4, 3, 3, 2]
# s = [5, 4, 3, 3, 8, 7, 100]
# we know [5,5] is better than [5,4] in any situation
# so only when [5,4] is not picked, we will start to think about [5,5]
# first we put the ones on the left into list before list is full
# then each time check new candidate
#   1. we know candidate has <= efficiency than anyone in the current list
#      since target = min(efficiency of all elements) * sum(speed of all elements)
#      the worst one in current list is the one with smallest speed
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pick = []
        res = speed_sum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            bisect.insort(pick, -s)
            speed_sum += s
            if len(pick) > k:
                speed_sum += pick.pop()
            res = max(res, speed_sum * e)
            """
            1. element in the list != element is taken into consideration
            2. before list is full, maximum target is:
                1) either current target (element is ignored)
                2) or updated target (element is picked)
                either way element is added into list 
            3. when list becomes full, we add current element then pop the one with smallest speed
                1) if current element is not the one being popped:
                    1- target is the same (element is ignored)
                    2- target is updated (element is picked)
                2) if current element is the one begin popped:
                    it has the smallest e and s, so target will not be updated
            """
        return res % (10**9+7)

    
# heap: same as above, just faster insertion/delection
# sorting: nlogn
# go through heap: klogk
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pick = []
        res = speed_sum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(pick, s)
            speed_sum += s
            if len(pick) > k:
                speed_sum -= heapq.heappop(pick)
            res = max(res, speed_sum * e)
        return res % (10**9 + 7)