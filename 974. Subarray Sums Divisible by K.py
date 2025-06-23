# prefix sum + hashmap 
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0 # prefix_sum from nums[0] to current element
        res = 0 
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1 

        for num in nums:
            prefix_sum += num
            remain = prefix_sum % k
            res += prefix_cnt[remain]
            prefix_cnt[remain] += 1

            """
            how the above part works:
            assume prefix_sum == 9 and k == 5
            then we are looking for previous prefix_sum 
            like -1, 4, 9, 14, etc
            so that (prefix_sum - previous prefix_sum) % k == 0
            this is the same as:
            previous prefix_sum % k == prefix_sum % k
            so go back to the example 
            9 % 5 = 4
            therefore we just need to find out how many
            previous prefix_sum % 5 == 4
            """
        
        return res