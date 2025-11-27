class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        We use binary search on the answer:
        - Let `t` be the time needed to complete at least totalTrips.
        - For any candidate time `t`, we can compute how many trips all drivers can make:
              sum(t // driver_time)
        - If this sum >= totalTrips, then `t` is sufficient and we try smaller times.
        - Otherwise, we need more time.
        """

        # Minimum possible time is 1
        left = 1
        # Maximum possible time occurs if the fastest driver does all the trips
        right = min(time) * totalTrips

        while left < right:
            mid = (left + right) // 2

            # Count how many trips can be completed in 'mid' time
            trips = 0
            for t in time:
                trips += mid // t
                # Early stop if already enough
                if trips >= totalTrips:
                    break

            # If we can make enough trips, try smaller time
            if trips >= totalTrips:
                right = mid
            else:
                left = mid + 1

        return left
