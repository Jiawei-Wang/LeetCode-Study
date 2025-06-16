# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# for two matching tuples, there are 8 combos
# for three: there are 8 + 8 * 2
# for four: there are 8 + 8 * 2 + 8 * 3
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        ans = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                ans += 8 * product_count[product]
                product_count[product] += 1

        return ans