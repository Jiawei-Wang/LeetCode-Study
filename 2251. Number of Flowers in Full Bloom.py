# sort + binary search
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(s for s, e in flowers)
        ends = sorted(e for s, e in flowers)

        res = []

        # at given time t:
        # flowers in bloom = flowers started <= t - flowers ended < t
        for t in people:
            started = bisect.bisect_right(starts, t)
            ended = bisect.bisect_left(ends, t)
            res.append(started - ended)

        return res
