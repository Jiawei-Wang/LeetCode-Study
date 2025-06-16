# monotone stack

# 1. what is monotonous increase stack: 
# its previous element < every element < its next element

# 2. how it is built
# for i in range(len(A)):
#     while in_stk and in_stk[-1] > A[i]:
#         in_stk.pop()
#     in_stk.append(A[i])

# 3. what problems can it solve:

#   1) find the previous smaller element of each element in an array
#   for example: [3, 7, 8, 4]
#   3: none, 7: 3, 8: 7, 4: 3
#   we want to get [-1, 0, 1, 0]
#   code: 
#   previous_less = [-1] * len(A)
#   in_stk = []
#   for i in range(len(A)):
#       while in_stk and A[in_stk[-1]] > A[i]:
#           in_stk.pop()
#       previous_less[i] = -1 if not in_stk else in_stk[-1]
#       in_stk.append(i)

#   2) also find the next smaller element of each element in an array
#   for example: [3, 7, 8, 4]
#   3: none, 7: 4, 8: 4, 4: none
#   we want to get [-1, 3, 3, -1]
#   code: 
#   next_less = [-1] * len(A)
#   in_stk = []
#   for i in range(len(A)):
#       while in_stk and A[in_stk[-1]] > A[i]:
#           x = in_stk.pop()
#           next_less[x] = i
#       in_stk.append(i)

# use monotonous increase stack in this problem:
# for example: [2, 9, 7, 8, 3, 4, 6, 1]
# for element 3: the previous smaller element is 2, the next smaller element is 1
# so with monotonous increase stack, we can find distance between 3 and 2, and 3 and 1
# one observation: all subarrays with 3 as minimum are:
# 9 7 8 3 
# 9 7 8 3 4 
# 9 7 8 3 4 6 
# 7 8 3 
# 7 8 3 4 
# 7 8 3 4 6 
# 8 3 
# 8 3 4 
# 8 3 4 6 
# 3 
# 3 4 
# 3 4 6
# in total 4 * 3 = 12 
# so sum of all minimum for these 12 subarrays is: 3 * 12
# so final answer for this problem is:
# sum(A[i] * left[i] * right[i])
# where left[i] is the distance between element A[i] and its previous smaller element
# and right[i] is the distance between element A[i] and its next smaller element

# return sum of all minimums in every subarray
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # 1. create the distance arrays
        n = len(A)
        left = [i + 1 for i in range(n)]     # Distance to previous smaller
        right = [n - i for i in range(n)]    # Distance to next smaller

        # 2. create the stacks for iteration
        in_stk_p = []  # Monotonic increasing stack for previous smaller
        in_stk_n = []  # Monotonic increasing stack for next smaller

        # one pass
        for i in range(n):
            # Previous smaller
            while in_stk_p and in_stk_p[-1][0] > A[i]:
                in_stk_p.pop()
            left[i] = i + 1 if not in_stk_p else i - in_stk_p[-1][1]
            in_stk_p.append((A[i], i))

            # Next smaller
            while in_stk_n and in_stk_n[-1][0] > A[i]:
                val, idx = in_stk_n.pop()
                right[idx] = i - idx
            in_stk_n.append((A[i], i))

        ans = 0
        mod = 10**9 + 7
        for i in range(n):
            ans = (ans + A[i] * left[i] * right[i]) % mod
        return ans