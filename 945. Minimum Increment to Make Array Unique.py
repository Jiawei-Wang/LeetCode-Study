# sorting nlogn
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0

        for i in range(1, len(nums)):
            # if current number is bigger than previous number, we do nothing
            # if current number is equal to previous number, current number += 1
            # if current number is smaller than previous number, 
            # which means we have used this number already, 
            # we need to bump this number to previous number + 1
            # for example [1, 2, 2, 3, 3]
            # [1, 2] are good, nothing needs to be done
            # second 2 needs to be bumped to 3
            # first 3 needs to be bumped to 4
            # second 3 needs to be bumped to 5
            if nums[i-1] >= nums[i]:
                answer += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        
        return answer


# counter: n + max (count from 1 to len(nums) + max(nums))
# for example [1, 1, 2, 2, 3, 7] (doesn't have to be sorted)
# then counter = {
#     1: 2
#     2: 2
#     3: 1
#     7: 1
# }
# start from 1, every key will keep value <= 1 and move the rest to next key
# max key is max(nums), plus len(nums) in case all elements in nums are max value
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        answer = 0
        for i in range(len(nums) + max(nums)):
            if count[i] > 1:
                extra = count[i] - 1
                count[i+1] += extra
                answer += extra
        return answer


# union find
# need to revisit this code 
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        hashmap = {}
        
        def find(num):
            if num not in hashmap:
                hashmap[num] = num
            else:
                hashmap[num] = find(hashmap[num]+1)
            return hashmap[num]
        
        return sum(find(num) - num for num in nums)
