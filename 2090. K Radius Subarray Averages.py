class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        window_size = 2 * k + 1

        if n < window_size:
            return answer

        # Initial window sum
        total = sum(nums[:window_size])
        answer[k] = total // window_size

        # Slide the window
        for i in range(k + 1, n - k):
            total += nums[i + k] - nums[i - k - 1]
            answer[i] = total // window_size

        return answer
