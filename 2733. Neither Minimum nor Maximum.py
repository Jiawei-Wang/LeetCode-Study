class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        big = None
        smo = None

        # every num is a unique one between 1 <= num <= 100
        for num in nums:
            if big == None and smo == None:
                big = num
            elif smo == None:
                smo, big = min(big, num), max(big, num)
            else:
                if num > big:
                    return big
                elif num > smo:
                    return num
                else:
                    return smo
        
        return -1
            