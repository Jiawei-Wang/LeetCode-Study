class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        left = dict()
        for index, value in enumerate(arr):
            left[value] = index

        for piece in pieces:
            if piece[0] not in left:
                return False
            
            start = left[piece[0]]
            length = len(piece)

            if arr[start:start+length] != piece:
                return False
            
            for number in piece:
                del left[number]
        
        return not left 
            
