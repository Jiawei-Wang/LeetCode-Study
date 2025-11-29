class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = defaultdict(int)

        count = 0
        for song in time:
            remain = song % 60
            need = 60 - remain

            if need == 60:
                count += hashmap[0]
            elif need in hashmap:
                count += hashmap[need]

            hashmap[remain] += 1
        
        return count
        
