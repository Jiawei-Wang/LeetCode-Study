class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        # key: first digit, value: number of elements with this first digit

        answer = 0

        for number in nums:
            string = str(number)
            first = int(string[0])
            last = int(string[-1])

            for key, value in hashmap.items():
                if math.gcd(last, key) == 1:
                    answer += value
            
            hashmap[first] += 1
    
        return answer

