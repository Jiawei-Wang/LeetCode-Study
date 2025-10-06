class Solution:
    def countCompleteSubarrays(self, A: List[int]) -> int:
        length = len(A)
        target = len(set(A)) # total number of unique values we need
        
        count = defaultdict(int) # freq
        res = 0
        i = 0 # left pointer

        for j in range(length): # for each subarray ending at j
            # we count the frequency of values
            count[A[j]] += 1
            while len(count) >= target: # then we move pointer i to find smallest subarray
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    del count[A[i]]
                i += 1
            res += i # so we have in total i subarrays that meet the target

        return res