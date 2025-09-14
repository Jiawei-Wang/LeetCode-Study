# if you reverse two adjacent elements, aka a swap
# you can generate any permutation group for the whole array
# (foundation of bubble sort)
# therefore if two arrays share the same elements (values and frequencies)
# you can always fransform one into the other with subarray reversals
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hashmap = defaultdict(int)
        for i in range(len(target)):
            hashmap[target[i]] += 1
            hashmap[arr[i]] -= 1
        
        for key,value in hashmap.items():
            if value != 0:
                return False
            
        return True