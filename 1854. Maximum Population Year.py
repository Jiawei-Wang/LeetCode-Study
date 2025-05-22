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


# sortedlist
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


# line sweep
from collections import defaultdict
class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        line = defaultdict(int)
        for birth, death in logs:
            line[birth] += 1
            line[death] -= 1

        max_population = 0
        current_population = 0
        ans_year = 0

        for year in sorted(line):
            current_population += line[year]
            if current_population > max_population:
                max_population = current_population
                ans_year = year

        return ans_year


# prefix sum: improvement from simulation
# simulation: for each person, mark all alive years
# prefix sum: only mark birth and death, then do the calculation by going one loop
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # key information: 1950 <= birth < death <= 2050
        # so we know the year array is small
        year = [0] * 101  # 1950 to 2050 => 101 years

        # first mark every birth and death on the array
        for birth, death in logs:
            year[birth - 1950] += 1
            year[death - 1950] -= 1

        max_num = year[0]
        max_year_index = 0

        # then we calculation the population of each year by going through every year's mark
        for i in range(1, 101):
            year[i] += year[i - 1]
            if year[i] > max_num:
                max_num = year[i]
                max_year_index = i

        return 1950 + max_year_index

