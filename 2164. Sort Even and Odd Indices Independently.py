class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        eve = [nums[i] for i in range(0, len(nums), 2)]
        odd = [nums[i] for i in range(1, len(nums), 2)]

        eve.sort()
        odd.sort(reverse=True)

        answer = []
        for i in range(len(odd)):
            answer.append(eve[i])
            answer.append(odd[i])
        if len(eve) > len(odd): # one extra at the end if nums is odd length
            answer.append(eve[-1])
        return answer