class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        occurrence = [0] * n # occurrence[i] = k: city i has k roads connected to it
        for road in roads:
            occurrence[road[0]] += 1
            occurrence[road[1]] += 1

        occurrence.sort()

        res = 0
        for i in range(n):
            res += occurrence[i] * (i + 1)

        return res
