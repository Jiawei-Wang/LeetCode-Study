# if a team has any stronger opponent, this team can't be the champion
# and that opponent can be a potential champion
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # start by assuming winner is 0-th team
        winner = 0

        # exam every team behind current winner
        # when winner = 0 it is easy to understand: 
        # we check all other teams to find the first team that is stronger than 0-th team
        # when winner = another team, the logic is:
        # since this team is guaranteed to be stronger than any team before it (handled by code below)
        # we only need to check teams behind it
        for opponent in range(len(grid)):

            # skip own team
            if opponent == winner:
                continue

            # if a team j behind current winner i is stronger than i
            # and since we know j is the first team that is strong than i
            # that means any team between i and j is weaker than j
            if grid[winner][opponent] == 0:
                winner = opponent
        
        return winner