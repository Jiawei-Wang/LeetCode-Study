# https://en.wikipedia.org/wiki/Josephus_problem

# simulation
class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        # use queue: O(n)
        # space: O(n)
        people = [i+1 for i in range(n)]
        curr = 0
        while n > 1:
            # find target index
            if curr + k - 1 < n:
                target = curr + k - 1
            else:
                target = (curr + k - 1) % n 
            # remove target
            people.pop(target)
            # change length
            n -= 1
            # find new current
            curr = target
        return people[0]



