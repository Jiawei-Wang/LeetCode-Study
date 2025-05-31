# first greedy can be proved to be optimal
# then in each iteration we add student to maximize profit
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def profit(pass_, total):
            return (pass_ + 1) / (total + 1) - pass_ / total

        heap = []
        total = 0

        for p, t in classes:
            total += p / t
            # Use a max heap by pushing negative profit
            heapq.heappush(heap, (-profit(p, t), p, t))

        while extraStudents:
            neg_gain, p, t = heapq.heappop(heap)
            total += -neg_gain  # adding the actual gain
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-profit(p, t), p, t))
            extraStudents -= 1

        return total / len(classes)
