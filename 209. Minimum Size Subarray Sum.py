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




# 2026
# brute force: pick all possible pairs, calculate sum for each pair n^3 
# prefix sum: pick all possible pairs, check sum_j - sum_i n^2
# binary search: for each i, find the cloest j behind it using prefix sum nlogn
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        for example: nums = [a, b, c, d]
        all possible subarrays are:
        starting at a: a, ab, abc, abcd
        starting at b: b, bc, bcd
        starting at c: c, cd
        starting at d: d
        to get sum(abc), we can't use prefix[c] - prefix[a]
        that will give a + b + c - a = b + c
        instead we need prefix[c] - prefix[0]: a + b + c - 0
        so if we need the sum of subarray nums[i:j+1]
        we need prefix[j] - prefix[i-1]
        """
        prefix = [0] # empty subarray has total = 0

        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        # for example prefix[3] = 10 means
        # first 3 elements at index = 0, 1, 2 have total = 10
        # nums[0:3] = 10

        # if sum of whole nums is still to small
        if prefix[-1] < target:
            return 0
        
        # else: we know there exists such subarray
        length = len(nums) 
        minimum_length = length # this subarray can be at most the whole nums

        for i in range(length):
        # prefix[i] is the part that will be deducted so i can go from
        # 0: empty subarray, to
        # length - 1: subarray with everything but the last element in nums
        # it makes no sense to add last element because that gives the full nums
        # then the only j is just prefix[-1] 
        # and prefix[j] - prefix[i] = 0 (whole nums - whole nums = nothing inside)

            # now we use binary search to find the smallest j such that 
            # prefix[j] - prefix[i] >= target
            left = i + 1 #  j starts at at least i+1 (1 element in the final subarray)
            right = length # ends at length (all elements in nums are in prefix[j])
            # len(prefix) = len(nums) + 1
            # so last element in prefix is prefix[length]

            while left != right:
                mid = (right - left) // 2 + left 
                subarray = prefix[mid] - prefix[i] 
                if subarray == target: # everything element in nums is positive so the subarray can't get shorter
                    minimum_length = min(minimum_length, mid - i)
                    break
                elif subarray > target: # try to shrink 
                    right = mid
                else: # try to expand
                    left = mid + 1
            
            # when left and right become the same, the subarray[i+1: right+1] may still be < target
            if prefix[right] - prefix[i] >= target:
                minimum_length = min(minimum_length, right - i)

        
        return minimum_length 

# slinding window: n
# expanding right then shrinking left is too complicated
# we should only care about right
# for every step right takes, find the biggest left
class Solution:
    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        
        left = 0
        total = 0
        
        for right, n in enumerate(nums):
            total += n
            while total >= target:
                # instead of updating result at the very last
                # update it for every step left takes
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1

        return result if result <= len(nums) else 0
