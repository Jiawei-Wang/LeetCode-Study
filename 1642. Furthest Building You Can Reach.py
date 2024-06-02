# use bricks for small gaps and ladders for big gaps
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        stand = 0 # which building we are standing on right now
        gap_bricks = [] # max_heap: gaps that are small and should use bricks
        heapq.heapify(gap_bricks)
        
        while stand < len(heights)-1:
            gap = heights[stand+1] - heights[stand]
            if gap <= 0: # free climb
                stand += 1
                continue
            else: 
                # first check if we have enough resources for this climb
                if bricks >= gap or ladders > 0:
                    stand += 1
                    # then update all resources
                    heapq.heappush(gap_bricks, -gap)
                    bricks -= gap
                    if bricks < 0:
                        biggest_gap = heapq.heappop(gap_bricks) * -1
                        bricks += biggest_gap
                        ladders -= 1
                else:
                    return stand

        return len(heights)-1
        