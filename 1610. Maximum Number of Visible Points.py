# convert all coordinates to radians
# sort the array
# use sliding window to find the longest window that satisfies arr[r] - arr[l] <= angle.
# Time complexity: O(NlogN)
# Space complexity: O(N)
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        arr = []
        extra = 0
        xx, yy = location
        
        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            # The math.atan2() method returns the arc tangent of y/x, in radians
            # Where x and y are the coordinates of a point (x,y).
            arr.append(math.atan2(y - yy, x - xx))
        
        arr.sort()
        arr = arr + [x + 2.0 * math.pi for x in arr]
        angle = math.pi * angle / 180
        
        l = ans = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans + extra