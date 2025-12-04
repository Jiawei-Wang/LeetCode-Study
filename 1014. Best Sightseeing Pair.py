# we want to get max value of values[i] + values[j] + i - j
# in other words: we want the maximum values[i] + i + values[j] - j
# so we need to keep track of maximum values[i] + i
# in the below code, we also let it -= 1 for each step we take
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # start with the first position
        answer = values[0] # answer stores global best pair, currently it only has first position as half of the pair
        previous = values[0] - 1 # previous stores the best previous position

        # then iterate through all other positions
        for value in values[1:]: # for each position
            answer = max(answer, previous + value) # first we check if we find a better pair: best previous + current value
            previous = max(previous, value) - 1 # then before we move onto next position, we update best previous
        
        return answer