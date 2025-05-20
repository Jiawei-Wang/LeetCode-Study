"""
given a list of votes and a list of time stamps for those votes
find which candidate is leading the election at given time

Constraints:
1 <= persons.length <= 5000
    meaning: at least 1 vote, at most 5000
times.length == persons.length
    meaning: each vote has 1 time stamp
0 <= persons[i] < persons.length
    meaning: at least 1 candidate, no more candidates than votes
0 <= times[i] <= 10^9
times is sorted in a strictly increasing order.
times[0] <= t <= 109
At most 10^4 calls will be made to q.
"""

class TopVotedCandidate:
    def __init__(self, persons, times):
        self.leads, self.times, count = [], times, {}
        lead = -1
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(lead, 0): lead = p
            self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]
        # bisect.bisect(array, value) returns the index where value should be inserted to maintain sorted order
        # after any existing entries of value (inserts to the right of equal values)


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)