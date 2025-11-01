class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # build starting window
        needed = k
        for i in range(k):
            if blocks[i] == "B":
                needed -= 1
        
        # iteration
        answer = needed
        for i in range(k, len(blocks)):
            needed -= blocks[i] == "B"
            needed += blocks[i-k] == "B"
            answer = min(answer, needed)
        return answer
