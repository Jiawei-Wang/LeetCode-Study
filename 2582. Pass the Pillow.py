class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # one loop (forward and back) takes n * 2 - 2 steps
        full_loop_steps = n * 2 - 2

        # so for last loop we have time % (n * 2 - 2) steps
        finished_loops, last_loop = divmod(time, full_loop_steps)
        
        # if last_loop < n - 1: we are on the way towards n
        # if last_loop > n - 1: we are on the way back
        # so distance from n is abs(n - 1- time)
        return n - abs(n-1-last_loop)