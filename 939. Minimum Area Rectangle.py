# brute force: check all quadruples
# everything we do is to 
# 1. avoid unnecessary comparisons (less computation)
# 2. have faster lookup (faster computation)
# basic idea: scan through every x, for each y pair (y1, y2) under this x
# see if they have been seen in previous xs 
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Group y-values by x
        x_to_ys = defaultdict(list)
        for x, y in points:
            x_to_ys[x].append(y)
        
        min_area = float("inf") # the return value 
        last_x_for_y_pair = {} # lookup table to remember last x where a (y1,y2) pair was seen
        
        # go from left to right, bottom to top
        for x in sorted(x_to_ys.keys()):
            ys = sorted(x_to_ys[x])
            
            # For each vertical pair of y’s in this column
            for i in range(len(ys)):
                for j in range(i + 1, len(ys)):
                    y1, y2 = ys[i], ys[j]
                    pair = (y1, y2)
                    
                    if pair in last_x_for_y_pair: # we found a smaller x with this pair
                        prev_x = last_x_for_y_pair[pair]
                        area = (x - prev_x) * (y2 - y1)
                        min_area = min(min_area, area)
                    
                    last_x_for_y_pair[pair] = x # update lookup table
                    # since we are moving to bigger xs, if multiple rectangles can be formed
                    # we should only use the right most one, therefore only keep the biggest x
                    # for example if we are currently at 10: (y1, y2)
                    # and we have 5: (y1, y2) and 8: (y1, y2)
                    # 5: (y1, y2) is not needed, and we can save time on comparisons
        
        return 0 if min_area == float("inf") else min_area
