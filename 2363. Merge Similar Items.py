class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashmap = dict()
        for item in items1:
            hashmap[item[0]] = [item[1]]
        
        for item in items2:
            if item[0] in hashmap:
                hashmap[item[0]].append(item[1])
            else:
                hashmap[item[0]] = [item[1]]

        answer = []
        for key, value in hashmap.items():
            answer.append([key, sum(value)])
        return sorted(answer)