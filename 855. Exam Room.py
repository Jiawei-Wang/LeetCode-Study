import bisect

class ExamRoom:

    def __init__(self, n: int):
        """
        Initializes the exam room with N seats, numbered from 0 to N-1.
        We track currently occupied seats in a sorted list.
        """
        self.n = n
        self.seats = []

    def seat(self) -> int:
        """
        Seats the next student to maximize the distance to their closest neighbor.
        If there are multiple such seats, minimizes the seat index.
        """
        # --- LOGIC CASE 1: The room is completely empty ---
        # Rule states the first student always sits in seat 0.
        if not self.seats:
            self.seats.append(0)
            return 0
        
        # --- LOGIC CASE 2: Consider the leftmost boundary (Seat 0) ---
        # If seat 0 is empty, the distance from 0 to the first seated student 
        # is exactly the index of that first student (self.seats[0]).
        max_dist = self.seats[0]
        best_seat = 0
        
        # --- LOGIC CASE 3: Scan the intervals between adjacent seated students ---
        # For any two adjacent students at 'left' and 'right', the optimal seat is
        # exactly in the middle. The distance to the closest person from the middle is (right - left) // 2.
        for i in range(len(self.seats) - 1):
            left = self.seats[i]
            right = self.seats[i + 1]
            dist = (right - left) // 2
            
            # We use strictly greater than (>) because if there's a tie in distance,
            # we must prefer the lower seat index (which we processed earlier).
            if dist > max_dist:
                max_dist = dist
                best_seat = left + dist
                
        # --- LOGIC CASE 4: Consider the rightmost boundary (Seat N - 1) ---
        # If the last seat is empty, the distance from the last student to the end
        # of the room is (N - 1) - self.seats[-1].
        # We use strictly greater than (>) here as well to respect the lowest-index rule.
        if (self.n - 1) - self.seats[-1] > max_dist:
            best_seat = self.n - 1
            
        # --- FINALIZATION ---
        # Maintain the sorted order of occupied seats using binary search insertion.
        # This keeps the array sorted in O(P) time where P is the number of people sitting.
        bisect.insort(self.seats, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        """
        A student leaves the seat p.
        Removes the seat from our tracking list.
        """
        # Removing an element from a Python list takes O(P) time
        # because elements after it must shift left.
        self.seats.remove(p)