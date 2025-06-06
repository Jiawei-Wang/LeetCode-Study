# backtracking
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(list(range(1, 10)), k, n, [], ans)
        return ans
    
    def dfs(self, nums, k, n, path, ans):
        if k < 0 or n < 0:
            return 
        if k == 0 and n == 0:
            ans.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ans)