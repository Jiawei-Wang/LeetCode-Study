# we need to find 3 edges connecting 4 nodes in a sequence
# can't be other shapes like: 0<->1, 0<->2, 0<->3
# and return the sequence with biggest sum of scores
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:        
        # For each node, precompute its top-3 neighbors (by score)
        # why 3 neighbors: the sequence has 4 nodes, so at most 3 will be connected to the picked node
        top3 = collections.defaultdict(list)

        def add_neighbor(a, b):
            heapq.heappush(top3[a], (scores[b], b))
            if len(top3[a]) > 3:
                heapq.heappop(top3[a])  # remove the smallest
        
        for a, b in edges:
            add_neighbor(a, b)
            add_neighbor(b, a)
        
        # for each edge (b, c), try all combinations:
        # a from top neighbors of b, and d from top neighbors of c
        ans = -1
        for b, c in edges:
            for score_a, a in top3[b]:
                for score_d, d in top3[c]:
                    if a not in (b, c) and d not in (b, c) and a != d:
                        ans = max(ans, scores[b] + scores[c] + score_a + score_d)
        return ans