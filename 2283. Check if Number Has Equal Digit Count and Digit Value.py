class Solution:
    def digitCount(self, num: str) -> bool:
        hashmap = defaultdict(int)
        lookup = [0] * 10

        for index, char in enumerate(num):
            digit = int(char)
            hashmap[digit] += 1
            lookup[index] = digit

        for index in range(10):
            if index in hashmap and hashmap[index] != lookup[index]:
                return False
        
        return True
