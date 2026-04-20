"""
starting and target positions don't matter
since we are on a infinitely big 2d plane
only the diff matters 
diff_x = fx - sx
diff_y = fy - sy

each move, we have 3 moves for each axis:
+1, +0, -1
but we only have 8 options since (+0, +0) doesn't exist

so now the question is whether or not we can get the diff with t steps

observations:
1. we can easily find minimum steps to cover diff:
   minimum_steps = max(abs(diff_x), abs(diff_y))
   keep going diagonally then straight 
2. if minimum_steps > t: then we can't get to target
   if minimum_steps == t: jobs done
   if minimum_steps < t: we need to take more steps
3. now we need to find a way to waste extra steps
   we can break any step into 2:
   for example +1, +1 can be +1, +0 then +0, +1
   for example +1, +0 can be +1, +1 then +0, -1
   and also we can take 2 steps to stay where we are
   so any number of extra steps can be wasted
4. except: if we have one extra step and need to stay where we are

so in summary:
1. if one extra step left and need to stay: False
2. else: if minimum_stesp >= t: always True
         else: always False
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        diff_x = abs(fx - sx)
        diff_y = abs(fy - sy)

        minimum_steps = max(diff_x, diff_y)

        # If start and finish are the same
        # you can't reach it in exactly 1 second because you must move.
        if minimum_steps == 0 and t == 1:
            return False
            
        # If the time given is at least the minimum distance, 
        # you can always reach it (by zig-zagging or walking away and back).
        return t >= minimum_steps


        