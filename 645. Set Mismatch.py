# 读题想法：题目要求从array中找出重复的元素以及缺失的元素

# 解法1：一次遍历，使用set寻找重复元素，使用另一个set寻找缺失元素
# Time n
# space 2n
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [-1,-1]
        duplicate = set()
        missing = set(n for n in range(1,len(nums)+1))

        for i in nums:
            if i in duplicate:
                ans[0] = i
            duplicate.add(i)

            missing.discard(i)
        ans[1] = missing.pop()
        return ans

# 解法2：sorting
# Time: nlogn (sorting使用logn)
# Space: logn (sorting使用logn)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = -1
        missing = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup = nums[i]
            elif nums[i] > nums[i-1]+1:
                missing = nums[i-1]+1
        # 因为无法检测缺失的是否为最后一个元素，所以使用这个句式
        return [dup, len(nums) if nums[-1]!= len(nums) else missing]
