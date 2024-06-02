class SeatManager:

    # n >= 1
    def __init__(self, n: int):
        self.seats = [i+1 for i in range(n)]
        heapq.heapify(self.seats)
    
    # For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
    def reserve(self) -> int:
        return heapq.heappop(self.seats)
        
    # For each call to unreserve, it is guaranteed that seatNumber will be reserved.
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)