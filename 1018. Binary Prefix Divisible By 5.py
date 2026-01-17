class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        binary_string = ""
        for i in range(len(nums)):
            binary_string += str(nums[i])
            dec_number = int(binary_string, 2)
            if dec_number % 5 == 0:
                answer.append(True)
            else:
                answer.append(False)
        return answer

