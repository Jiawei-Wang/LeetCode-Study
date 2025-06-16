# grid is small (m, n <= 70) and numbers are small (mat[i][j] <= 70)
# so brute force is not too bad
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        nums = {0}
        for row in mat:
            # keep all possible sums so far
            nums = {x + num for x in row for num in nums}
        
        return min(abs(target-num) for num in nums)


# since every number is positive: 1 <= mat[i][j] <= 70
# we don't have to deal with negative numbers
# first choose minimum element of each row to create minimum sum: possible_min
# if possible_min > target, then we have no choice but to accept it
# if possible_min <= target, then we only need to consider the range [possible_min, 2*target-possible_min]
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # 1. get minimum sum
        possible_min = sum(min(row) for row in mat)
        
        # 2.1 case one:
        if possible_min > target: 
            return possible_min - target
        
        # 2.2 case two: 
        nums = {0}
        for row in mat: 
            # still the same thing, go through each row
            # but we only keep numbers that are within the range
            # (possible_min <= number already satisfies)
            nums = {x + i for x in row for i in nums if x + i <= 2*target - possible_min}
        return min(abs(target - x) for x in nums)