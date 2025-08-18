class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        answer = float("inf")
        nums.sort()
        length = len(nums)
        for i in range(length//2):
            answer = min(answer, (nums[i]+nums[length-i-1])/2)
        return answer


# 1 <= nums[i] <= 50 
# so we can use counting sort
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        length = len(nums)
        freq = [0] * 51
        xMin, xMax = 50, 1

        for x in nums:
            freq[x] += 1
            xMin = min(xMin, x)
            xMax = max(xMax, x)
        # now we have 
        # 1. a freq list
        # 2. min/max element in the input list

        minAv = 50.0 # nothing is bigger than 50 so set initial value to 50 instead of inf
        i, j = xMin, xMax

        # then go through freq list and calculate the averages
        while length > 0:
            while i < j and freq[i] == 0:
                i += 1
            while i < j and freq[j] == 0:
                j -= 1
            if i > j:
                break

            minAv = min(minAv, (i + j) / 2.0)

            freq[i] -= 1
            if freq[i] == 0:
                i += 1

            freq[j] -= 1
            if freq[j] == 0:
                j -= 1

            length -= 2

        return minAv