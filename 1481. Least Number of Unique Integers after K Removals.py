# Solution 1: Counter + sort: TLE
# time O(n+nlogn) space O(n)
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # 1. count arr and get Counter
        # 2. sort arr based on each value's freq
        # 3. remove the first k 
        # 4. return the set of remaining arr
        return len(set(sorted(arr, key=lambda x: (Counter(arr)[x], x))[k:]))


# Solution 2: Counter + min heap
# time O(n+klogn) space O(n)
from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = list(Counter(arr).values())
        heapq.heapify(freq)
        while k > 0:
            k -= heapq.heappop(freq)
            # after removing current value
            # if k == 0: we get what we want
            # if k < 0: last value can only be removed partially
        return len(freq) + (k < 0)
        
        
# Solution 3: Counter + array
# time O(n) space O(n)
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # first: create occurrence list
        # for example: arr = [4, 3, 1, 1, 3, 3, 2]
        # occurrence list = [0, 2, 1, 1, 0, 0, 0, 0]
        count = Counter(arr)
        occurrence_count = [0] * (len(arr) + 1)
        for v in count.values():
            occurrence_count[v] += 1

        # second: some variables
        remaining = len(count) # number of unique values that remain
        occur = 1 # index for where we are on the occurrence list, currently at index = 1

        # third: do the calculation
        while k > 0:
            if k - occur * occurrence_count[occur] >= 0:
                k -= occur * occurrence_count[occur]
                remaining -= occurrence_count[occur]
                occur += 1
            else:
                return remaining - k // occur
        
        return remaining

