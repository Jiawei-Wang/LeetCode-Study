# solution 1: double loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return None


# solution 2: hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use dictionary as hashmap
        # https://www.w3schools.com/python/python_dictionaries.asp
        Map = {}
        for i in range(0, len(nums)):
            Map[nums[i]] = i
        # search for complement
        for i in range(0, len(nums)):
            complement = target - nums[i]
            # 记得检查两个数的下标是否相同
            if complement in Map and Map[complement] != i:
                return [i, Map[complement]]
        return None


# solution 3: hashmap one pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in Map and Map[complement] != i:
                return [i, Map[complement]]
            else:
                Map[nums[i]] = i
        return None


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index in range(len(nums)):
            left = target - nums[index]
            if left in hashmap:
                return [index, hashmap[left]]
            else:
                hashmap[nums[index]] = index
        
