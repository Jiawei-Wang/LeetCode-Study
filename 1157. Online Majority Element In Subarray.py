# brute force: check the subarray for each query
from collections import Counter
from typing import List

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        # Slice the array and count frequencies
        counts = Counter(self.arr[left:right + 1])
        
        # Find if any element meets the threshold
        for num, count in counts.items():
            if count >= threshold:
                return num
        return -1


#Boyer-Moore Voting + Binary Search
import bisect
from typing import List

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.loc = defaultdict(list)
        # Store all indices for each number
        for i, val in enumerate(arr):
            self.loc[val].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        # Step 1: Boyer-Moore Voting to find a candidate
        candidate = -1
        count = 0
        for i in range(left, right + 1):
            if count == 0:
                candidate = self.arr[i]
                count = 1
            elif self.arr[i] == candidate:
                count += 1
            else:
                count -= 1
        
        # Step 2: Verify the candidate using binary search
        if candidate != -1:
            indices = self.loc[candidate]
            # Find how many times candidate appears between left and right
            l_idx = bisect.bisect_left(indices, left)
            r_idx = bisect.bisect_right(indices, right)
            if (r_idx - l_idx) >= threshold:
                return candidate
                
        return -1