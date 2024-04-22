"""
if any element in a triplet is bigger than target: this triplet cannot be used anywhere
if an element in a triplet is equal to target: this target is achievable
"""
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1 = False
        t2 = False
        t3 = False

        for tri in triplets:
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                continue
            if tri[0] == target[0]:
                t1 = True
            if tri[1] == target[1]:
                t2 = True
            if tri[2] == target[2]:
                t3 = True

        return t1 and t2 and t3