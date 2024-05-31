class Solution:
    def leastBricks(self, walls: List[List[int]]) -> int:
        gaps = [] # 2d list, each list is all gaps for a wall
        positions = set() # all positions that contain at least a gap (no need to start from all possible positions)
        
        # get all gaps
        for wall in walls:
            gap = set()
            length = 0
            for i in range(len(wall)-1):
                length += wall[i]
                gap.add(length)
                positions.add(length)
            gaps.append(gap)

        # check how many blocks for a position
        def blocked(position):
            count = 0
            for gap in gaps:
                if position not in gap:
                    count += 1
            return count

        # try all positions and find the one with minimum blocks
        answer = len(walls)
        for position in positions:
            answer = min(answer, blocked(position))
        return answer
        
        
# we can further reduce run time by using 
# a hashmap to store the position with gaps
# and return the position with most gaps directly
class Solution:
    def leastBricks(self, walls: List[List[int]]) -> int:
        gap_frequency = {} # key: gap, value: number of times this gap shows in walls
        max_frequency = 0 
        
        for wall in walls:
            gap = 0 
            for brick in wall[:-1]:  
                gap += brick
                gap_frequency[gap] = gap_frequency.get(gap, 0) + 1
                max_frequency = max(gap_frequency[gap], max_frequency)
                
        return len(walls) - max_frequency 