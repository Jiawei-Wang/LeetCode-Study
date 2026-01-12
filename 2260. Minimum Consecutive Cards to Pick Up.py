class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        lookup = dict()
        length = len(cards)
        shortest = length + 1
        for index in range(length):
            card = cards[index]
            if card in lookup:
                shortest = min(shortest, index - lookup[card] + 1)
            lookup[card] = index
        return shortest if shortest != length + 1 else -1