class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        
        for i in range(len(nums)-2):
            # 如果第一个数字大于0, 则三个数总和必然大于0
            if nums[i] > 0: break
            
            # 如果此时遍历到的数字和前一个相同则直接略过
            if i != 0 and nums[i] == nums[i-1]: continue
            
            # 问题被分解为two sum: 在nums[i]的后面找到两个数字之和为-nums[i]
            target = -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append((nums[i], nums[l], nums[r]))
                    # 两个while循环排除重复答案
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    # 然后再各步进一步
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res

if __name__ == "__main__":
    # test case 1: should return [[-1,-1,2],[-1,0,1]]
    nums = [-1,0,1,2,-1,-4]
    case1 = Solution()
    print(case1.threeSum(nums))


# 05-03-2022
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The idea is to sort an input array and then run through all indices of a possible first element of a triplet. 
        For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array. 
        Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth like that.
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # prevent duplicate first element
                continue
                
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]: # prevent duplicate for second element 
                        l += 1
                    while l < r and nums[r] == nums[r-1]: # prevent duplicate for third element
                        r -= 1
                    l += 1; r -= 1 # still need to find all possible combinations start with i
        return res
    
    
        """
        理解算法：在two sum 2的基础上再加一层for loop
        难点：two sum 2是找到一个可能组合，此题需要找到所有的组合，同时又需要避免重复
        重复有两层含义：1. [i, l, r]和[i, r, l]是重复，2. 两个值相同但下标不同的元素也是重复，比如[0, -5, 5]和[0, -5, 5]中的0和5都是同一个元素但-5来自两个不同的元素
        此解法巧妙之处：同一个元素不会出现两次，值相同的元素被忽略
        """


# 2025
# turn 3sum into 2sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()  # sort so duplicates are easier to detect
        
        # for every first element
        for i in range(len(nums)-2):
            # do it like 2sum
            target = -nums[i]
            hashset = set()
            for j in range(i+1, len(nums)):
                if target - nums[j] in hashset:
                    answer.add((nums[i], target-nums[j], nums[j]))  # store as tuple
                hashset.add(nums[j])
        
        return [list(triplet) for triplet in answer]


# faster with two pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # for every first element
        for i in range(len(nums)-2):
            # skip the duplicate first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # use two pointers
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # if we find an answer, we need to find a new second element
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res