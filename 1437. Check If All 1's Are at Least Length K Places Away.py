class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        distance = float("inf")
        for num in nums:
            if num == 0:
                distance += 1
            else:
                if distance < k:
                    return False
                else:
                    distance = 0
        return True