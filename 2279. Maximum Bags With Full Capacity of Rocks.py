class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []
        for i in range(len(capacity)):
            diff.append(capacity[i] - rocks[i])
        diff.sort()
        count = 0
        index = 0
        while additionalRocks and index < len(diff):
            if additionalRocks >= diff[index]:
                additionalRocks -= diff[index]
                count += 1
                index += 1
            else:
                break
        return count