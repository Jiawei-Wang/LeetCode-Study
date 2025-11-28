import random

class Solution:

    def __init__(self, nums: List[int]):
        # Store original array
        self.original = list(nums)
        self.array = list(nums)

    def reset(self) -> List[int]:
        # Reset to the original configuration
        self.array = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        # Fisher-Yates shuffle
        n = len(self.array)
        for i in range(n):
            # Pick a random index from i to n-1
            j = random.randrange(i, n)
            # Swap
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()