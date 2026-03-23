class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = defaultdict(int)
        for char in target:
            counter[char] += 1
        
        exist = defaultdict(int)
        for char in s:
            if char in counter:
                exist[char] += 1
        
        smallest = float("inf")
        for key, value in counter.items():
            have = exist[key]
            copy = have // value
            smallest = min(smallest, copy)
        return smallest

        