# too much memory
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = [[0 for _ in range(k+1)] for _ in range(k+1)]
        # score[x][y] = z: taking x cards from beginning + y cards from end will give total score z

        for r in range(1, k+1): # only pick from beginning
            score[r][0] = score[r-1][0] + cardPoints[r-1] 
            # for example r = 1: pick 1 card from beginning: score = 0 + cardPoints[0]

        for c in range(1, k+1): # only pick from end
            score[0][c] = score[0][c-1] + cardPoints[-c] 
            # for example c = 1: pick 1 card from beginning: score = 0 + cardPoints[-1]

        # start from 1-th row and 1-th col
        for r in range(1, k+1):
            for c in range(1, k-r+1): # at most (k-r) card from end
                score[r][c] = score[r-1][c] + cardPoints[r-1]

        best = 0
        for r in range(k, -1, -1):
            for c in range(0, k+1):
                best = max(best, score[r][c])
        return best


# sliding window
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # 1. Start by taking all k cards from the left
        current_score = sum(cardPoints[:k])
        max_score = current_score
        
        n = len(cardPoints)
        
        # 2. "Slide" the window
        # pick one from end and discard one from beginning
        for i in range(1, k + 1):
            # Remove card at index (k - i)
            # Add card at index (n - i)
            current_score = current_score - cardPoints[k - i] + cardPoints[n - i]
            
            if current_score > max_score:
                max_score = current_score
                
        return max_score