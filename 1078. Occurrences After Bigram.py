class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        data = text.split()
        for i in range(len(data)-2):
            if data[i] == first and data[i+1] == second:
                ans.append(data[i+2])
        return ans
                
