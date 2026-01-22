class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        table = dict()
        for index, num in enumerate(nums):
            table[num] = index
        
        for op in operations:
            current = op[0]
            target = op[1]
            index = table[current]
            table[target] = index
            del table[current]
        
        answer = [0] * len(nums)
        for key, value in table.items():
            answer[value] = key
        return answer