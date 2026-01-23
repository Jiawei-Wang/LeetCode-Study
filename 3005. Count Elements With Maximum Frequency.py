class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        answer = 0
        most_freq = 0
        for key, value in counter.items():
            if value > most_freq:
                most_freq = value
                answer = most_freq
            elif value == most_freq:
                answer += most_freq 
        return answer