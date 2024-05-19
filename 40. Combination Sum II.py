# a normal dfs on decision tree will generate duplicates, for example [1, 1, 5], target = 6
# we can pick first 1 and 5 to get [1, 5]
# we can pick second 1 and 5 to get [1, 5]
# so we need to get rid of duplicates, in a way that:
# we won't have two [1, 5]
# but [1, 1] is still available if target = 2
# why not let answer = set() and check if [1, 5] is inside?
# list is not hashable 
# so to prevent duplicates, we need to:
# 1. sort the array
# 2. use a for loop inside dfs
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  
        answer = []

        def dfs(index, total, path):
            if total > target or index > len(candidates):
                return
            elif total == target:
                answer.append(path)
                return
            else:
                """
                logic: we can pick element with same value but at most one for same dfs loop

                1. for current path, we want to find next element to add to path
                   (not for each element, we want to see if we want to add it or not)
                2. so we go through every element in the remaining list
                3. if it's the first one, we can add it, for example 1 can be added to path [1] to form [1, 1]
                4. if it's not first one and it's the same as previous one, we do nothing
                   because we know previous one has been used already

                for example sorted list [1, 1, 1, 5] target = 2
                1. we go into the dfs with empty path, and every element in list [1, 1, 1, 5] is available 
                2. we check if a valid path can be found by using every element as first one in path
                3. we pick element 1 with index = 0 as first one, then go into inner dfs 
                    1) now the available list becomes [1, 1, 5]
                    2) element 1 with index = 1 can be picked to form valid path [1, 1]
                    3) element 1 with index = 2 will be skipped
                    4) element 5 is picked but path is not valid
                4. now we return back to outer dfs with [1, 1, 1, 5] being available
                5. we pick element 1 with index = 1, it is skipped
                6. we pick element 1 with index = 2, it is skipped
                7. we pick element 5 with index = 3, go into inner dfs
                """
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    dfs(i+1, total+candidates[i], path+[candidates[i]])

        dfs(0, 0, [])
        return answer