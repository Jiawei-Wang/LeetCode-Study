class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [1]
        best = 1
        hashmap = dict()
        hashmap[arr[0]] = 1

        for i in range(1, len(arr)):
            curr = arr[i]
            target = curr - difference
            if target not in hashmap:
                dp.append(1)
                hashmap[curr] = 1
            else:
                dp.append(hashmap[target] + 1)
                hashmap[curr] = hashmap[target] + 1
                best = max(best, hashmap[curr])
        
        return best