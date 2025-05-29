# after cars are assigned, calculating total time needed is easy
# finding the optimal car assignment is hard, which is the core of this question
#
# dp is not ideal for this question since:
# there are no clear subquestion and step 
# ranks (list of mechanics) can be very long and cars can be a big int, so possible combos are too many
#
# but instead, if we set a time goal, it's easy to find maximum amount of cars that we can repair
# so binary search on time is useful
# min time: 1
# max time: maxRank * cars^2
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, cars * cars * max(ranks)

        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)

            if cars_repaired < cars:
                low = mid + 1
            else:
                high = mid

        return low