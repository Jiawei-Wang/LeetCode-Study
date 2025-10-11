class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = defaultdict(list)
        answer = []
        for index, size in enumerate(groupSizes):
            hashmap[size].append(index)
            if len(hashmap[size]) == size:
                answer.append(hashmap[size])
                hashmap[size] = []
                
        return answer