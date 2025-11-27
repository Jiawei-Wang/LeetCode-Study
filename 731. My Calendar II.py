# sweeping line
class MyCalendarTwo:

    def __init__(self):
        # Stores +1 at start, -1 at end for sweep-line
        self.map = {}

    def book(self, start: int, end: int) -> bool:
        # Add event
        self.map[start] = self.map.get(start, 0) + 1
        self.map[end] = self.map.get(end, 0) - 1

        count = 0
        # Iterate in sorted order like TreeMap
        for key in sorted(self.map.keys()):
            count += self.map[key]
            
            if count > 2:
                # Revert changes
                self.map[start] -= 1
                if self.map[start] == 0:
                    del self.map[start]

                self.map[end] += 1
                if self.map[end] == 0:
                    del self.map[end]

                return False

        return True

        
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)


# better
class MyCalendarTwo:

    def __init__(self):
        self.booked = []    # a list of events
        self.overlaps = []  # a list of intervals (two events are already here)

    def book(self, start: int, end: int) -> bool:
        # Step 1: Reject event if it overlaps with any existing interval
        for s, e in self.overlaps:
            if start < e and end > s:
                return False

        # Step 2: Check for overlaps with self.booked
        new_overlap = []
        for s, e in self.booked:
            if start < e and end > s:
                # Overlap exists; this becomes a new interval
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                new_overlap.append((overlap_start, overlap_end))

        # Step 3: All checks passed → add new overlaps to self.overlaps
        self.overlaps.extend(new_overlap)

        # Step 4: Also commit the event to booked
        # can't do it before step 2 since we need to read from self.booked first
        self.booked.append((start, end))

        return True
