"""
1. we start with w, and try to get the maximum possible w
2. for at most k steps:
    1) each step we can pick an index
    2) w_left = w - capital[index], w_left must >= 0 at all times
    3) w_gain = w + profits[index] 
       (profit is pure profit so w_gain doesn't start from w_left)

Greedy:
1. sort projects by capital in ascending order
2. add available projects (w >= capital[index]) into heap
3. each time pick most profitable one, then update w, and add new available proejcts
"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        # now projects are sorted from cheap to expensive capital
        # also within same capital, projects are sorted from less profitable to more profitable

        maximizeCapital = []
        i = 0 # we start from first project
        while k > 0: # we can pick at most k projects
            # for each time
            # first we find new available projects with current w
            while i < n and projects[i][0] <= w: 
                heapq.heappush(maximizeCapital, -projects[i][1])
                i += 1
            # if we don't have available projects, we stop
            if not maximizeCapital:
                break
            # then we pick most profitable one and update w
            w -= heapq.heappop(maximizeCapital)
            k -= 1
        return w