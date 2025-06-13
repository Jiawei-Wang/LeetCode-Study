class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # first read the input string "order"
        # order of chars is represented by values and stored in hashmap
        hashmap = dict()
        for index, char in enumerate(order):
            hashmap[char] = index

        # then we group chars in input string "s" together
        # we first create 26 groups
        construct = [""] * 26
        for char in s:
            if char in hashmap:
                construct[hashmap[char]] += char
            else: 
                # if a char is not in order, it means order is guaranteed to be shorter 
                # than 26, so construct[25] is empty and we can use it
                # therefore on line 11 construct was set to 26 not 27
                construct[25] += char
        return "".join(construct)
            