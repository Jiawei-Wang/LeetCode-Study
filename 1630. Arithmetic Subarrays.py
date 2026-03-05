# brute force
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)

        answer = []

        for i in range(m):
            left = l[i]
            right = r[i]

            subarray = nums[left:right+1]

            subarray.sort()

            is_arithmetic = True
            diff = subarray[1] - subarray[0]
            for i in range(len(subarray)-1):
                if subarray[i+1] - subarray[i] != diff:
                    is_arithmetic = False
                    break
            
            answer.append(is_arithmetic)
        
        return answer
            




