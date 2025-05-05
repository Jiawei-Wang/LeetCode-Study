# bucket sort: 
# 1. create buckets
# 2. put each number into corresponding bucket based on value range
# 3. some buckets may have zero number, some may have multiple numbers
# 4. sort each bucket and combine them together


# use bucket sort in this question
# we just use the buckets, but don't sort within buckets

# for example nums = [3,14,15,83,6,4,19,20,40]
# create n-1 buckets, in this case 9-1=8 buckets
# why n-1: we have n-1 gaps between min and max number, max number goes into last bucket
# since min=3, max=83, each bucket will be: [3,13), [13,23), ..., [73,83]
# then we put each number into a bucket 
# 0: [3, 6, 4]
# 1: [14, 15, 19, 20]
# 3: [40]
# 7: [83]

# biggest gap will not happen within a bucket, because:
# for gaps between numbers, at least one of the gaps must be greater than or equal to (hi - lo)//(n - 1)
# since bucket size is (hi - lo)//(n - 1), any two numbers within the same bucket must be closer together than that size
# So no bucket can contain the maximum gap — it must lie between buckets

class Solution:
    def maximumGap(self, nums):
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        B = defaultdict(list)

        for num in nums:
            ind = n-2 if num == hi else (num - lo)*(n-1)//(hi-lo)
            B[ind].append(num)
        # B: 
        # 0: [3, 6, 4]
        # 1: [14, 15, 19, 20]
        # 3: [40]
        # 7: [83]
            
        cands = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        # cands = [[3, 6], [14, 20], [40, 40], [83, 83]]

        return max(y[0]-x[1] for x,y in zip(cands, cands[1:]))
        # zip(cands, cands[1:]) pairs each element in cands with the next one.
        # cands is:     [[3, 6], [14, 20], [40, 40], [83, 83]]
        # cands[1:] is:         [[14, 20], [40, 40], [83, 83]]
        # zip(cands, cands[1:]) produces:
        # ([3, 6], [14, 20])
        # ([14, 20], [40, 40])
        # ([40, 40], [83, 83])
        