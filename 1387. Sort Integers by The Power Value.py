# brute force
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def steps(number):
            counter = 0
            while number != 1:
                if number % 2:
                    number = number * 3 + 1
                else:
                    number //= 2
                counter += 1
            return counter
    
        hashmap = dict()
        for number in range(lo, hi + 1):
            hashmap[number] = steps(number)
        array = sorted(hashmap, key = hashmap.get)
        return array[k-1]


# faster steps function
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        steps_hashmap = dict()
        
        def steps(number):
            counter = 0
            curr = number
            while curr != 1:
                if curr in steps_hashmap:
                    return counter + steps_hashmap[curr]

                if curr % 2:
                    curr = curr * 3 + 1
                else:
                    curr //= 2
                counter += 1
            
            steps_hashmap[number] = counter
            return counter
    
        hashmap = dict()
        for number in range(lo, hi + 1):
            hashmap[number] = steps(number)
        array = sorted(hashmap, key = hashmap.get)
        return array[k-1]


# optimal 
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # instead of only adding end result to hashmap
        # add every step result to hashmap
        memo = {1: 0}
    
        def get_steps(n):
            path = []
            curr = n
            # find the path from number to an known number (or 1 if there is no known number on the path)
            while curr not in memo:
                path.append(curr) 
                if curr % 2 == 0:
                    curr //= 2
                else:
                    curr = 3 * curr + 1

            steps_for_curr = memo[curr]
            for i, node in enumerate(reversed(path)):
                memo[node] = steps_for_curr + i + 1
            return memo[n]

        # Use a list of tuples to sort by value then by key (tie-breaker)
        res = []
        for i in range(lo, hi + 1):
            res.append((get_steps(i), i))
            
        # Sorting tuples automatically handles (value, tie-breaker_key)
        res.sort()
        return res[k-1][1]