# 读题想法：题目要求从array中找出重复的元素以及缺失的元素


# 解法0：一次遍历，使用set寻找重复元素，使用另一个set寻找缺失元素
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


# 解法4：使用hashmap记录nums中所有元素，然后再从1到n遍历查询map
# Time：n
# Space：n
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = {}
        dup = -1
        missing = -1

        # 初始化一个dictionary
        for i in nums:
            # 如果有值则+1，如果没有则设定为1
            hashmap[i] = hashmap.setdefault(i, 0)+1

        # 遍历
        for j in range(1, len(nums)+1):
            if j in hashmap:
                if hashmap[j] == 2:
                    dup = j
            else:
                missing = j

        return [dup,missing]


# 解法5：extra array
# Time: n
# Space: n
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 使用一个额外的array来记录每个数字的出现次数
        arr = [0] * (len(nums)+1)
        dup = -1
        missing = -1

        # 遍历nums中元素
        for i in nums:
            arr[i] +=1

        # 遍历arr来找到答案
        for j in range(1,len(arr)):
            if arr[j] == 0:
                missing = j
            elif arr[j] == 2:
                dup = j
        return [dup,missing]
