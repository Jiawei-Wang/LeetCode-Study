class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        prefix_odd = []
        prefix_evn = []
        # prefix_odd[i] = k:
        # at index i: all odd index numbers before it sum up to k 
        # so for 0-th number: prefix_odd and prefix_evn are both 0 

        odd_total = 0
        evn_total = 0

        for index, number in enumerate(nums):
            prefix_odd.append(odd_total)
            prefix_evn.append(evn_total)
            
            is_odd_index = index % 2
            if is_odd_index:
                odd_total += number
            else:
                evn_total += number



        suffix_odd = deque([])
        suffix_evn = deque([])

        odd_total = 0
        evn_total = 0

        for index in range(len(nums)-1, -1, -1):
            number = nums[index]
            suffix_odd.appendleft(odd_total)
            suffix_evn.appendleft(evn_total)
            
            is_odd_index = index % 2
            if is_odd_index:
                odd_total += number
            else:
                evn_total += number

                
        answer = 0
        for i in range(len(nums)):
            if prefix_odd[i] + suffix_evn[i] == prefix_evn[i] + suffix_odd[i]:
                answer += 1
        return answer