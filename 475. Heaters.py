"""
1. For each house, find its position between those heaters (thus we need the heaters array to be sorted).
2. Calculate the distances between this house and left heater and right heater, get a MIN value of those two values. Corner cases are there is no left or right heater.
3. Get MAX value among distances in step 2. It's the answer.
"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def binsearch(nums, target) :
            i = 0; j = len(nums)
            while i < j :
                mid = i + (j-i) // 2
                if nums[mid] < target : i = mid + 1
                else : 
                    j = mid
            return i
            
        heaters.sort()
        result = float('-inf')
        for house in houses :
            index = binsearch(heaters, house)
            leftHeaterDistance = house - heaters[index - 1] if index > 0 else float('inf')
            rightHeaterDistance = heaters[index] - house if index < len(heaters) else float('inf')
            result = max(result , min(leftHeaterDistance, rightHeaterDistance))
        
        return result

# math
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i+2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r