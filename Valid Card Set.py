"""
04/29/2024 Google phone screen

check if a given set of cards is valid:
input: list of strings
output: boolean

a set of cards is valid if:
1. it is of at least 3 cards
AND
2. all cards are of same number and different shape: 
["3D", "3H", "3S", "3C"] (doesn't have to be full 4)
OR
3. all cards are of same shape and different number, and numbers are consecutive
["9D", "10D", "JD", "QD"]
"""

def is_valid_set(cards):
    length = len(cards)
    if length <= 2:
        return False
        
    def match_index(num):
        if num == "A":
            return 0
        elif num == "J":
            return 10
        elif num == "Q":
            return 11
        elif num == "K":
            return 12
        else:
            return int(num)-1
        
    def is_consecutive(existing):
        for i in range(first_exist, last_exist+1):
            if existing[i] == False:
                return False
        return True
    
    target_shape = cards[0][-1]
    target_number = cards[0][:-1]

    existing = [False] * 13
    first_index = match_index(target_number)
    existing[first_index] = True
    first_exist = first_index
    last_exist = first_index
    
    for index in range(1, length):
        card = cards[index]
        shape = card[-1]
        number = card[:-1]
        
        if shape != target_shape and number != target_number: 
            return False
        else:
            idx = match_index(number)
            existing[idx] = True
            first_exist = min(first_exist, idx)
            last_exist = max(last_exist, idx)
    return is_consecutive(existing) or first_exist == last_exist

            
# length check
print(is_valid_set(["3D", "4D", "5D"])) # should true
print(is_valid_set(["3D", "4D"])) # should be false

# consecutive number check
print(is_valid_set(["9D", "10D", "JD"])) # should be true
print(is_valid_set(["KD", "AD", "2D"])) # should be false

# shape check
print(is_valid_set(["3D", "3H", "3C"])) # should be true