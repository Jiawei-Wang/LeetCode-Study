class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        team_num = len(votes[0]) # number of teams 
        hashmap = dict()

        for vote in votes:
            for index, team in enumerate(vote):
                if team not in hashmap:
                    hashmap[team] = [0 for _ in range(team_num)] 
                hashmap[team][index] += 1

        sorted_keys = sorted(hashmap.keys(), key=lambda x: ([-count for count in hashmap[x]], x))
        # create a tuple with reversed value + letter
        # for example: 
        # hashmap = {'A': [5, 0, 0], 'B': [0, 2, 3], 'C': [0, 3, 2]}
        # these get passed into sorting: 
        # ([-5, 0, 0], 'A')
        # ([0, -2, -3], 'B')
        # ([0, -3, -2], 'C')
        
        return "".join(sorted_keys)
