class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        length = len(nums)
        i = 0
        window_index = 0
        while i < length:
            if nums[i] == key:
                window_index = max(i - k, window_index)
                while window_index < length and window_index <= i + k:
                    result.append(window_index)
                    window_index += 1
            i += 1

        return result