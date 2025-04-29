class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        hashmap = dict()
        for i in range(min(k + 1, len(nums))):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                return True
        
        for i in range(k+1, len(nums)):
            del hashmap[nums[i-k-1]]
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                return True
        return False

