class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = int(math.sqrt(area))
        while l <= area:
            if area % l == 0 and l >= (area // l):
                return [l,area//l]
            l += 1
        return [area,1]
        
