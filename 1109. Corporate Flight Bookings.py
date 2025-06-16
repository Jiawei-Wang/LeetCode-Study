class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        accumulate = [0] * (n + 2) 

        for booking in bookings:
            first = booking[0]
            second = booking[1]
            seats = booking[2]
            accumulate[first] += seats
            accumulate[second+1] -= seats
        
        answer = []
        current = 0
        for i in range(1, n+1):
            current += accumulate[i]
            answer.append(current)
        return answer