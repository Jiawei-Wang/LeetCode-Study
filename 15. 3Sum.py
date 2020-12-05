class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        
        for i in range(len(nums)-2):
            # 如果第一个数字大于0, 则三个数总和必然大于0
            if nums[i] > 0: break
            
            # 如果此时遍历到的数字和前一个相同则直接略过
            if i != 0 and nums[i] == nums[i-1]: continue
            
            # 问题被分解为two sum: 在nums[i]的后面找到两个数字之和为-nums[i]
            target = -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append((nums[i], nums[l], nums[r]))
                    # 两个while循环排除重复答案
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    # 然后再各步进一步
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res

if __name__ == "__main__":
    # test case 1: should return [[-1,-1,2],[-1,0,1]]
    nums = [-1,0,1,2,-1,-4]
    case1 = Solution()
    print(case1.threeSum(nums))