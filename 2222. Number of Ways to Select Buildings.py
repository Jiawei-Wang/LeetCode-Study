# 101 or 010
class Solution:
    def numberOfWays(self, s: str) -> int:
        count_zero = 0
        count_one = 0

        length = len(s)

        array = []

        for index in range(length):
            current = s[index]

            if current == "1":
                array.append(count_zero)
                count_one += 1
            else:
                array.append(count_one)
                count_zero += 1
        
        answer = 0
        for index in range(1, length-1):
            if s[index] == "1":
                answer += array[index] * (count_zero - array[index])
            else:
                answer += array[index] * (count_one - array[index])
        return answer




        