class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        length = len(hand)
        
        # corner case: cards can't be evenly divided
        if length % groupSize:
            return False
        
        # method to build the group
        def build_group():
            k = groupSize
            head = min(counter.keys())
            while k != 0:
                k -= 1
                if head not in counter:
                    return False
                else:
                    counter[head] -= 1
                    if counter[head] == 0:
                        del counter[head]
                    head += 1
            return True

        # counter 
        counter = dict()
        for card in hand:
            if card not in counter:
                counter[card] = 1
            else:
                counter[card] += 1

        group_number = length // groupSize
        while group_number != 0:
            # build current group
            group_number -= 1
            if not build_group():
                return False
        return True


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0: # a key can only be exhausted when it's the head of a group
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True