class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        jump = [0] + [float('inf')] * (length-1)
        for i in range(length):
            forward = nums[i]
            for j in range(1, forward+1):
                if i+j < length and jump[i+j] == float('inf'):
                    jump[i+j] = jump[i]+1
        return jump[-1]        


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        cur_end = 0
        cur_farthest = 0
        for i in range(len(nums)-1):
            cur_farthest = max(cur_farthest, i + nums[i])
            if i == cur_end:
                jump += 1
                cur_end = cur_farthest
        return jump