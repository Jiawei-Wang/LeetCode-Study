class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(num):
            if num == 1:
                return False
            if num == 2:
                return True

            upperbound = int(math.sqrt(num)+1)
            for i in range(2, upperbound + 1):
                if num % i == 0:
                    return False
            return True
        
        length = len(nums)
        answer = 0
        for i in range(0, length):
            num1 = nums[i][i]
            
            if is_prime(num1):
                answer = max(answer, num1)
            
            num2 = nums[i][length - i - 1]

            if is_prime(num2):
                answer = max(answer, num2)
            
        return answer

