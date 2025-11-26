"""
find subarray with biggest sum, with at most 1 deletion allowed

for each index i, there are two choices

1. no deletion yet:
no_del[i] = max subarray sum ending at i with 0 deletions used
and this is the same as Kadane algorithm
no_del[i] = max(nums[i], no_del[i-1] + nums[i])

2. already did deletion:
one_del[i] = max subarray sum ending at i with 1 deletion used
    1) if deletion happened on nums[i]
    one_del[i] = no_del[i-1]
    2) if deletion happened eariler
    one_del[i] = one_del[i-1] + nums[i]
so in total 
one_del[i] = max(one_del[i-1] + nums[i],  no_del[i-1])

so the answer if max of both states
answer = max(answer, no_del[i], one_del[i])

initial conditions: i = 0
no_del[0] = nums[0]
one_del[0] = -inf  (can't delete before the first element)
"""
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_del = arr[0]       # max sum ending here with 0 deletions
        one_del = float('-inf')  # max sum ending here with 1 deletion
        ans = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]

            # compute new states
            new_one_del = max(one_del + x, no_del)   # delete x or continue deleted-subarray
            new_no_del = max(no_del + x, x)          # normal Kadane

            # update
            one_del = new_one_del
            no_del = new_no_del

            # best so far
            ans = max(ans, one_del, no_del)

        return ans
