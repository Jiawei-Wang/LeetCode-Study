# 读题想法：题目要求从array中找出重复的元素以及缺失的元素


# 解法1：brute force
# 从1到n尝试每一个数字，查看其在nums中是否出现两次或者没有出现
# Time：n^2
# Space：1
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        missing = -1
        for i in range(1,len(nums)+1):
            count = 0
            for j in nums:
                if i == j:
                    count += 1
            if count == 2:
                dup = i
            if count == 0:
                missing = i
        return [dup,missing]


# 解法2：better brute force
# 在解法1基础上修改：如果已经找到dup和missing，就停止继续遍历
# Time：n^2
# Space：1
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        missing = -1
        for i in range(1,len(nums)+1):
            count = 0
            for j in nums:
                if i == j:
                    count += 1
            if count == 2:
                dup = i
            elif count == 0:
                missing = i
            if dup > 0 and missing > 0:
                break
        return [dup,missing]


# 解法3：sorting
# 先sort，然后遍历寻找dup和missing
# Time：nlogn （sorting使用nlogn)
# Space：nlogn （sorting使用nlogn）
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
        # 注意下面这句：因为无法检测缺失的是否为最后一个元素，所以使用这个句式
        return [dup, len(nums) if nums[-1]!= len(nums) else missing]







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
