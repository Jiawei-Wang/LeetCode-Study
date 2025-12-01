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


# use local path: 
# space: O(n^2)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(start, path): # start: the index of the number we are standing on
            # first check if requirement is satisfied
            if len(path) >= 2:
                answer.append(path)     # no need to copy, we never mutate path

            used = set()

            # then pick next number
            for i in range(start, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in used:
                    continue

                used.add(nums[i])
                # pass a NEW path (no mutation)
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return answer
