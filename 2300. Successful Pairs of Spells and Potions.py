# n*m: for every spell, check every potion
# mlogm + nlogm: sort potions first, then binary search on potions for each spell
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        length = len(potions)
        answer = []

        for spell in spells:
            target = math.ceil(success / spell) # potion has to be >= target

            l = 0
            r = length - 1

            # corner case: no such potion exists
            if potions[r] < target:
                answer.append(0)
                continue

            # it is guaranteed at least one exists
            while l < r:
                mid = l + (r-l)//2
                if potions[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            answer.append(length - l)

        return answer


