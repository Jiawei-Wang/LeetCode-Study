# reservior sampling algorithm
# to give fair chance of randomly picking a sample from a set of unknown size
# for first sample: 1/1 chance pick
# for second sample: 1/2 chance pick (current candidate 1/2 chance keep)
# for third sample: 1/3 chance pick (current candidate 2/3 chance keep)
# .....
# for n-th sample: 1/n chance pick (current candidate (n-1)/n chance keep)
import random 
class Solution:
    def __init__(self, nums: List[int]):
        self.rnd = random.Random()      
        self.hashmap = defaultdict(list)
        for index, number in enumerate(nums):
            self.hashmap[number].append(index) 

    def pick(self, target: int) -> int:
        result = -1
        count = 0
        for num in self.hashmap[target]:
            count += 1
            if self.rnd.randint(1, count) == 1: # chance of picking 1 from [1, n] is 1/n
                result = num
        return result        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# speed up with built-in 
class Solution:

    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])