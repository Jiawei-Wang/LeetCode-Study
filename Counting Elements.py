from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        dictionary = Counter(arr)
        count = 0
        for i in dictionary:
            if i+1 in dictionary:
                count += dictionary[i]
        return count
