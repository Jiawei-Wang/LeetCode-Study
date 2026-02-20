"""
question:
for n numbers, the return value is:
    1 * num1 + 2 * num2 + 3 * num3 + ... + n * numn
find the biggest return value when:
    1. numbers can be rearranged
    2. any number can be dropped 
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # for the order of dishes:
        # dish with bigger score will be at the end
        # for whether or not to drop a dish:
        # if keeping it gives better result, it should be kept
        
        satisfaction.sort()
        res = total = 0 
        # total is the sum of score of current dishes 
        # so each time when we pick a new dish, every dish gets 1 more unit time 
        # therefore res += total
        
        # each iteration, we pick the highest score dish
        # for the result:
        # all existing dishes will collectively += total
        # new added dish will += dish score
        # so if dish score + total > 0: we should keep this dish
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res