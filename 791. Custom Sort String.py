class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = dict()
        for i in range(len(order)):
            hashmap[order[i]] = i
        construct = [""] * 26
        for char in s:
            if char in hashmap:
                construct[hashmap[char]] += char
            else: 
                # if a char is not in order, it means order is guaranteed to be shorter 
                # than 26, so construct[25] is empty and we don't need construct[26]
                construct[25] += char
        return "".join(construct)
            