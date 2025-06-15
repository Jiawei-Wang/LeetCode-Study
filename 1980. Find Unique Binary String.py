# input: n binary numbers each of length n
# output: a binary number of same length that is new
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # math: if I create a number that
        # first digit is not the same as the first given number
        # second digit is not the same as the second given number
        # .....
        # n-th digit is not the same as the n-th given number
        # then it's a brand new number
        answer = ""
        for index, number in enumerate(nums):
            if number[index] == "0":
                answer += "1"
            else:
                answer += "0"
        return answer