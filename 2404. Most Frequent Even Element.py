class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashmap = {}
        val = 10**6 # keep track of the smallest answer
        freq = 0 # keep track of the greatest frequency
        for num in nums:
            if num % 2 == 0:
                if num in hashmap: 
                    hashmap[num]+=1
                else: 
                    hashmap[num]=1

                # Update smallest with greatest frequency
                if hashmap[num] > freq or (hashmap[num] == freq and num < val):
                    val, freq = num, hashmap[num]
        
        return -1 if freq == 0 else val
        