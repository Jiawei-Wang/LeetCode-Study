class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(start):
            if len(path) >= 2:
                res.append(path[:])  # Add a copy of the current subsequence

            used = set()  # Prevent duplicate picks at this depth
            # for example [4, 6, 7, 7]
            # there are two 7s
            # we can only have [4, 6, 7] once 

            for i in range(start, len(nums)):
                # Skip if:
                # 1. nums[i] < last element in path (violates non-decreasing)
                # 2. nums[i] already used at this recursion level (avoids duplicates)
                if (path and nums[i] < path[-1]) or nums[i] in used:
                    continue

                used.add(nums[i])
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res
