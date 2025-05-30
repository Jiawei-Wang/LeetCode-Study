class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split() 
        cnt = len(words)
        spaces = text.count(' ')
        gap = 0 if cnt == 1 else spaces // (cnt - 1)
        trailing_spaces = spaces - gap * (cnt - 1) 
        return (' ' * gap).join(words) + ' ' * trailing_spaces        
        
        
            
        