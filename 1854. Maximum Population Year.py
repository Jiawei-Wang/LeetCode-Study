# sort + heap
import heapq
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # input is not sorted, so heap can't work on that
        logs.sort()

        # put current alive people in a heap
        alive = [logs[0][1]]
        heapq.heapify(alive)
        population = 1 # population = size of alive heap
        max_population = 1 
        earliest_year = logs[0][0]

        # update heap for each new person
        for person in logs[1:]:
            while alive and alive[0] <= person[0]:
                heapq.heappop(alive)
                population -= 1

            heapq.heappush(alive, person[1])
            population += 1
            
            if population > max_population:
                max_population = population
                earliest_year = person[0]

        return earliest_year


# still same sort nlogn, same insertion logn
# but better bulk removal
# sortedlist deletion of multiple elements: logn + k, where k is number of deletions
from sortedcontainers import SortedList
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()  # sort by birth year
        
        alive = SortedList()
        alive.add(logs[0][1])  # first person's death year
        population = 1
        max_population = 1
        earliest_year = logs[0][0]

        for birth, death in logs[1:]:
            # Remove all who died before or at this birth year
            idx = alive.bisect_right(birth)
            if idx > 0:
                del alive[:idx]
                population -= idx

            alive.add(death)
            population += 1

            if population > max_population:
                max_population = population
                earliest_year = birth

        return earliest_year

