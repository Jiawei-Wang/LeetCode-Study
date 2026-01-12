class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def is_even(num):
            return num % 2 == 0

        if is_even(nums[0]):
            even_flag = False
        else:
            even_flag = True
        
        for num in nums[1:]:
            if is_even(num) != even_flag:
                return False
            
            even_flag = not even_flag
        
        return True
            