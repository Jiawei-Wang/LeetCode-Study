class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        digit = [int(char) for char in str(n)]
        counter = defaultdict(int)
        for d in digit:
            counter[d] += 1
        
        answer = 0
        least_freq = float("inf")
        for key, value in counter.items():
            if value < least_freq:
                least_freq = value
                answer = key
            elif value == least_freq:
                answer = min(answer, key)
        
        return answer


        