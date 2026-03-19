"""
thoughts:
greedy? sliding window? dp?
all elements are positive so sum only increases
so finding the smallest element in subarray is the key
1. prefix sum 
2. two extra arrays to store:
    index of last element in the front that is smaller than current element
    index of first element in the back that is smaller than current element
so for each index:
    window = first index in the back - last index in the front
    sum = prefix sum of first index - prefix sum of last index
    total = sum * current element
"""
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_sum = [] # prefix_sum[i] = k: sum of nums[0: i+1] is k
        total = 0

        prefix_index = [] # prefix_index[i] = j: nums[j] is the last element in the front that is smaller than nums[i]
        stack = []
        for index, value in enumerate(nums):
            total += value
            prefix_sum.append(total)

            while stack and stack[-1][0] >= value:
                stack.pop()
            if stack:
                prefix_index.append(stack[-1][1])
            else:
                prefix_index.append(-1)
            stack.append((value, index))

        suffix_index = deque([]) # suffix_index[i] = j: nums[j] is the first element in the back that is smaller than nums[i]
        stack = []
        for index in range(n-1, -1, -1):
            value = nums[index]

            while stack and stack[-1][0] >= value:
                stack.pop()
            if stack:
                suffix_index.appendleft(stack[-1][1])
            else:
                suffix_index.appendleft(n)
            stack.append((value, index))

        
        best = 0
        for i in range(n):
            left_index = prefix_index[i]
            if left_index == -1:
                first_prefix = 0
            else:
                first_prefix = prefix_sum[left_index]

            right_index = suffix_index[i]
            if right_index == n:
                second_prefix = prefix_sum[n-1]
            else:
                second_prefix = prefix_sum[right_index-1]
        
            total = second_prefix - first_prefix
            product = total * nums[i]
            best = max(product, best)
        return best % 1000000007




