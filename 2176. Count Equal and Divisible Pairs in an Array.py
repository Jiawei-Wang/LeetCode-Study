class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(list)
        for index, value in enumerate(nums):
            hashmap[value].append(index)

        count = 0
        for array in hashmap.values():
            n = len(array)
            for i in range(n-1):
                for j in range(i+1, n):
                    if array[i] * array[j] % k == 0:
                        count += 1
        return count