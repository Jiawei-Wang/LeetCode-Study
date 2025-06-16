# n^2: similar to three sum
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        # for every possible 3rd number
        for k in range(len(nums) - 1, 1, -1):
            # we try to find eligible 1st and 2nd numbers
            # key point is to use two pointers, so time complexity is o(n)
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # all elements between i and j are bigger than i
                    # so any of them + j + k can form triangle
                    count += j - i
                    j -= 1 # this j is finished, move on to smaller j
                    # we don't have to reset i to 0 because current i
                    # is the smallest to satisfy i + j > k
                    # with j becoming smaller, any smaller i will 
                    # make i + j > k not true
                else: # current i + j is too small, try bigger i
                    i += 1

        return count

"""
for a valid triangle with side a, b, c:
    a + b > c
    a + c > b
    b + c > a
in above case, since k >= i and k >= j:
    i + k > j is always true
    j + k > i is always true
    so we just need i + j > k to be true
"""
