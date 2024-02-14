class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = 0
        counter = dict()
        for num in nums:
            length += 1
            counter[num] = counter[num] + 1 if num in counter else 1
        return [key for key, value in counter.items() if value > length/3]


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # since the requirement is finding the majority for more than ceiling of [n/3]
        # the answer would be less than or equal to two numbers.
        if not nums:
            return []
        
        count1, count2, candidate1, candidate2 = 0, 0, 5, 99 # candidate1 and candidate2 can be any value
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]