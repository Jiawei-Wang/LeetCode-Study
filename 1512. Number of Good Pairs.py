# solution1: 暴力解，两层循环
# Time: n^2
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    ans += 1
        return ans


# solution2: hashmap，遍历数组，在每个位置上时寻找已经出现同值的次数
# Time: n
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 使用dictionary来实现java中map的功能
        Map = {}
        count = 0
        for num in nums:
            # get() method: https://www.tutorialspoint.com/python/dictionary_get.htm
            count += Map.get(num, 0)
            # 如果没有value，放入0+1，如果已有value，+1
            if num not in Map:
                Map[num] = 1
            else: Map[num] += 1

        return count


# solution 3: sorting
# Time: nlogn
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # sorted() and sort(): https://discuss.codecademy.com/t/what-is-the-difference-between-sort-and-sorted/349679
        nums.sort()
        count = 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                count += j-i
            else:
                i = j
        return count    
