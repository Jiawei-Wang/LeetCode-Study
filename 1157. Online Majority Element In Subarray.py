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