# sort 
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()

        start = nums[0][0]
        end = nums[0][1]
        total = 0

        for i in range(1, len(nums)):
            if nums[i][0] > end:
                total += end - start + 1
                start = nums[i][0]
            end = max(end, nums[i][1])

        return total + end - start + 1
    

# without sort 
class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        v = [0] * 102  # 1 <= start <= end <= 100
        ans = 0
        total = 0

        for start, end in nums:
            v[start] += 1
            v[end + 1] -= 1

        for i in range(1, 101):
            total += v[i]
            if total != 0:
                ans += 1

        return ans
