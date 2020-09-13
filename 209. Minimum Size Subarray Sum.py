# 解法1: 暴力解
# Time: n^3
# Space: 1
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 注意:
        # 1. subarray可以只有一个元素;
        # 2. 不一定有答案, 此时应该返回0
        ans = float('inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) >= s:
                    ans = min(ans, j-i+1)
        return ans if 0 < ans <= len(nums) else 0


# 解法2: 在解法1基础上改进计算subarray sum的时间, 使用一个额外array保存sum
# Time: n^2
# Space: n
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 先把sum算完
        sum_array = []
        total = 0
        for number in nums:
            total += number
            sum_array.append(total)

        # 再遍历
        ans = float('inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                '''
                下面这段代码的愿意是获得从i到j的sum, 因为sum = sum_array[j] - sum_array[i-1],
                可能导致下标出界, 所以先判断 i 的大小
                second = sum_array[i-1] if i>= 1 else 0
                if sum_array[j] - second >= s:
                    ans = min(ans, j-i+1)
                '''
                # 使用这个语法来避免上面的繁琐
                sum_this = sum_array[j] - sum_array[i] + nums[i]
                if sum_this >= s:
                    ans = min(ans, j-i+1)

        return ans if 0 < ans <= len(nums) else 0


# 解法3: binary search, 对解法2进行改良, n用于遍历nums, logn用于二分法找到对应的另一半
class Solution:
    def minSubArrayLen(self, target, nums):
        # 先计算sums
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n # 因为原始数据在计算完后就不再需要, 所以干脆拿来储存sums, 用以节约空间

        result = len(nums) + 1 # 任何大于len(nums)的值都可以

        # 对于每个从0开始到right为止, 大于target的sum, right不动, 找到left
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    # 二分法helper, 输入的参数为:
    # left = 0, right = 当前right所在下标, nums array(事实上是sums array), target, 以及right此时对应的sum
    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left



# 解法4: 双指针/滑动窗口
# Time: n
class Solution:
    def minSubArrayLen(self, s, nums):
        total = left = 0
        result = len(nums) + 1
        # right每前进一步, left就走到对应位置, 记录result的最小值
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1

        return result if result <= len(nums) else 0
