class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        length = len(nums)
        distance = []
        for i in range(1, length):
            distance.append(nums[i]-nums[i-1])

        answer = []
        for i in range(length):
            left_gaps = i
            left_index = i-1

            right_gaps = length - i - 1
            right_index = i

            total = 0
            while left_gaps != 0:
                total += left_gaps * distance[left_index]
                left_gaps -= 1
                left_index -= 1
            while right_gaps != 0:
                total += right_gaps * distance[right_index]
                right_gaps -= 1
                right_index += 1
            answer.append(total)
        return answer
        

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        # First element: total distance from nums[0] to all others
        for i in range(1, n):
            ans[0] += nums[i] - nums[0]

        # Use previous result to build the rest efficiently
        for j in range(1, n):
            diff = nums[j] - nums[j - 1]
            ans[j] = ans[j - 1] + diff * j - diff * (n - j)

        return ans