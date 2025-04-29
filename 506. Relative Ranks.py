class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_indices = sorted(range(len(score)), key=lambda i: -score[i])
        ranks = [0] * len(score)
        for rank, idx in enumerate(sorted_indices, start=1):
            if rank == 1:
                title = "Gold Medal" 
            elif rank == 2:
                title = "Silver Medal"
            elif rank == 3:
                title = "Bronze Medal"
            else:
                title = str(rank)
            ranks[idx] = title
        return ranks
