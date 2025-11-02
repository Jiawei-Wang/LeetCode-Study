class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            total = 0
            while num != 0:
                total += num % 10
                num //= 10 
            return total

        def two_biggest(array):
            biggest = -float("inf")
            second = -float("inf")
            for num in array:
                if num > biggest:
                    second, biggest = biggest, num
                elif num > second:
                    second = num
            return biggest + second  

        hashmap = defaultdict(list)
        for num in nums:
            hashmap[digit_sum(num)].append(num)
        
        answer = -1
        for key, value in hashmap.items():
            if len(value) <= 1:
                continue
            answer = max(answer, two_biggest(value))
        return answer


        