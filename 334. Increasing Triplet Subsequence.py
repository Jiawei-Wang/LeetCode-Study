class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

"""
understanding:
1. first always points to the smallest number in the whole array
2. second != inf means we already found a valid and smaller first
3. first may point to something else (for example: [1,0,2,0,-1,3] where first will eventually point to -1)
4. but as long as we have a valid second and have another number larger than second, we can return true
"""


# walk through the array with 3 flags
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for n in nums:
            if n <= first: # 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False