"""
math problem

for two numbers a and b to be equal by adding/subtracting x:
their difference must be divisible by x: (a - b) % x == 0
therefore: a % x == b % x (proof not provided)
so it means: all numbers must have same remainder to have an answer

now we know when an answer exists, we just need to find it
imagine all the numbers are points on a 1d line
I need to pick a target point T such that sum of all distances abs(num - T) is minimized

before I know where T is, imagine a random point t is picked
and there are l numbers smaller than t and r numbers bigger than t
if r > l (more numbers > t than < t) and we move t one unit to the right side:
this will decrease the distance for all r numbers but increase distance for all l numbers
and overall this is a good move since net distance gain is negative
so we keep moving t until net distance gain becomes 0
and that target is the T we need
net distance gain == 0 means r == l, which means T is the median number in all numbers
"""

# sort to find median: nlogn
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 1. Flatten the 2D grid into a 1D list
        nums = []
        for row in grid:
            nums.extend(row)
        
        # 2. Sort to find the median easily
        nums.sort()
        
        # 3. Check if all numbers are "compatible" with x
        # They must all share the same remainder when divided by x
        ref_mod = nums[0] % x
        for n in nums:
            if n % x != ref_mod:
                return -1
        
        # 4. Use the median as the target value
        median = nums[len(nums) // 2]
        
        # 5. Calculate the total operations
        operations = 0
        for n in nums:
            operations += abs(n - median) // x
        return operations



# quickselect: O(n)
import random
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        # 1. Flatten the grid
        nums = [val for row in grid for val in row]
        n = len(nums)
        
        # 2. Check if a solution is possible
        rem = nums[0] % x
        for num in nums:
            if num % x != rem:
                return -1
        
        # 3. Quickselect to find the median element
        def quickselect(arr, k):
            pivot = random.choice(arr)
            left = [v for v in arr if v < pivot]
            mid = [v for v in arr if v == pivot]
            right = [v for v in arr if v > pivot]
            
            # Is the k-th element in left, mid, or right?
            if k < len(left):
                return quickselect(left, k)
            elif k < len(left) + len(mid):
                return mid[0]
            else:
                return quickselect(right, k - len(left) - len(mid))
        
        median = quickselect(nums, n // 2)
        
        # 4. Calculate total operations
        return sum(abs(num - median) // x for num in nums)