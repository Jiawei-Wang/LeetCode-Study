class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        def get_width(char):
            index = ord(char) - ord('a')
            wide = widths[index]
            return wide

        curr = 0
        total = 1
        for char in s:
            wide = get_width(char)
            if curr + wide < 100:
                curr += wide
            elif curr + wide == 100:
                total += 1
                curr = 0
            else:
                total += 1
                curr = wide 
        
        return [total, curr] if curr != 0 else [total - 1, 100]
