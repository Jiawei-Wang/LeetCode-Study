# sort difficulty and worker: nlogn + mlogm
# then go through difficulty and worker: n + m
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        res = i = best = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            res += best
        return res


# create a map then binary search on it
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Create a map (difficulty -> best profit for that difficulty)
        jobs = dict()
        for d, p in zip(difficulty, profit):
            jobs[d] = max(jobs.get(d, 0), p)
        diffs = sorted(jobs.keys())
        best = 0
        for d in diffs:
            best = max(best, jobs[d])
            jobs[d] = best  

        # Binary search
        diff_list = diffs
        profit_list = [jobs[d] for d in diff_list]
        res = 0
        for w in worker:
            i = bisect_right(diff_list, w) - 1
            if i >= 0:
                res += profit_list[i]
        return res
