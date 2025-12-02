"""
You are given a list of events, where each event is a tuple:

(service_id, timestamp, event_type)

service_id is an integer

timestamp is a non-negative integer

event_type is either "Start" or "End"

the list is sorted by timestamp

A Start event means the service begins running at the given timestamp, and an End event means it stops.

The list is valid: for each service, every Start is followed by an End, and every End corresponds to a previous Start.

A service may have multiple start/end pairs throughout the list.

You are also given an integer timeout.

A service has a proper timeout if:

end_timestamp - start_timestamp >= timeout

When this happens, the actual timeout moment is:

start_timestamp + timeout

Your task is to find the earliest proper timeout across all services and return:

(service_id, timeout_time)

If no service times out, return None.

Example:

Events:
(1, 0, "Start")
(2, 1, "Start")
(1, 2, "End")
(3, 6, "Start")
(2, 7, "End")
(3, 8, "End")

timeout = 3

Explanation:
Service 1 runs 0 to 2 → no proper timeout
Service 2 runs 1 to 7 → proper timeout, and real timeout happened at time 1 + 3 = 4
Service 3 runs 6 to 8 → no proper timeout

Output: (2, 4)
"""
import heapq

def first_timeout(events, timeout):
    # events are already sorted by timestamp
    active = {}              # service_id -> start_time
    heap = []                # (timeout_time, service_id, start_time)

    for sid, ts, et in events:
        # before handling this event, check heap for expired timeouts
        while heap and heap[0][0] <= ts:
            t_out, s, start_t = heapq.heappop(heap)
            if s in active and active[s] == start_t:   # still active
                return s, t_out

        if et == "Start":
            active[sid] = ts
            heapq.heappush(heap, (ts + timeout, sid, ts))

        else:  # End
            if sid in active:
                del active[sid]

    # After all events, remaining active services might timeout afterward
    while heap:
        t_out, s, start_t = heapq.heappop(heap)
        if s in active and active[s] == start_t:
            return s, t_out

    return None


# Example usage
events = [
    (1, 0, "Start"),
    (2, 1, "Start"),
    (1, 2, "End"),
    (3, 6, "Start"),
    (2, 7, "End"),
    (3, 8, "End"),
]

print(first_timeout(events, 3))  # (2, 5)
