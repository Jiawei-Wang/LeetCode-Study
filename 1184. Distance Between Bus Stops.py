class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # corner case: start stop number > destination stop number
        start, destination = min(start, destination), max(start, destination)
        return min(sum(distance[start:destination]), sum(distance[destination:])+sum(distance[0:start]))