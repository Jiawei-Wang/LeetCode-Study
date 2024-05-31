class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if length == 1:
            if n == 1:
                return not flowerbed[0]
            else:
                return True
        
        count = 0
        if not flowerbed[0] and not flowerbed[1]:
            count += 1
            flowerbed[0] = 1

        for i in range(1, length-1):
            if not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                count += 1
                flowerbed[i] = 1
        
        if not flowerbed[-2] and not flowerbed[-1]:
            count += 1

        return count >= n
            


            


        