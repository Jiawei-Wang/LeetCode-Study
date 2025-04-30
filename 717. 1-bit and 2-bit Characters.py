class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # only one 0
        if len(bits) == 1: 
            return True

        # case 1
        # if there is a 0 before last 0
        # it means it must be either 0 or 10
        # and last 0 is not part of it
        if bits[-2] == 0:
            return True
        
        # case 2
        # if there is a 1 before last 0
        # we don't know if last 0 is part of it
        # go through the whole list
        i = 0
        while i < len(bits)-1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return True if i == len(bits)-1 else False
        