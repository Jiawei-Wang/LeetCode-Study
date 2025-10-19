class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to make it easier to skip duplicates
        res = [] 
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:]) 
                # list is mutable in python and res.append(path) will store the reference
                # and the reference will be empty at the end so all elements in res are empty
                # path[:] creates a shallow copy 
                # (a new list object containing the same elements at that moment)
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates — only use the first unused duplicate
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res
