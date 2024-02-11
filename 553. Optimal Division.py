class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        """
        X1/X2/X3/../Xn will always be equal to (X1/X2) * Y, no matter how you place parentheses. 
        i.e no matter how you place parentheses, X1 always goes to the numerator and X2 always goes to the denominator. 
        Hence you just need to maximize Y. And Y is maximized when it is equal to X3 *..*Xn. 
        So the answer is always X1/(X2/X3/../Xn) = (X1 *X3 *..*Xn)/X2
        """
        if not nums: return ""
        
        if len(nums) == 1: return str(nums[0])
        if len(nums) == 2: return str(nums[0]) + "/" + str(nums[1])
        ans = str(nums[0]) + "/(" + str(nums[1])
        for i in range(2, len(nums)):
            ans += "/" + str(nums[i])
        ans += ")"
        return ans
        