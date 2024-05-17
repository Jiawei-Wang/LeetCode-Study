# nums is sorted with all values being unique
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        length = len(nums)

        if length == 0:
            return answer
        if length == 1:
            answer.append(str(nums[0]))
            return answer

        string = str(nums[0])
        head = nums[0]

        for i in range(1, length):
            if nums[i] - nums[i-1] > 1: # if i is the start of a new string: we append string and create new string
                if nums[i-1] != head: # to prevent string like "6->6"
                    string += "->" + str(nums[i-1])
                answer.append(string)
                string = str(nums[i])
                head = nums[i]
                if i == len(nums) - 1:
                    answer.append(string)
            else: # if i is extending current string: we do nothing
                if i == len(nums) -1:
                    answer.append(string + "->" + str(nums[i]))

        return answer


        