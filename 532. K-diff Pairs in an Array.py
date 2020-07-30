class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # corner case
        if not nums or k < 0:
            return 0

        # new hashmap
        Map = {}
        count = 0
        for i in nums:
            if i in Map:
                Map[i] += 1
            else:
                Map[i] = 1

        # loop through hashmap
        for i in Map:
            if k == 0:
                if Map[i] >= 2:
                    count += 1
            else:
                if i+k in Map:
                    count += 1

        return count
        
