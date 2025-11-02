class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if len(start) != len(result): 
            return False
        
        # check L R orders are the same
        if start.replace('X','') != result.replace('X', ''): 
            return False
        
        n = len(start)
        Lstart = [i for i in range(n) if start[i] == 'L']
        Lend = [i for i in range(n) if result[i] == 'L']
        
        Rstart = [i for i in range(n) if start[i] == 'R']
        Rend = [i for i in range(n) if result[i] == 'R']
        
		# check L positions are correct
        for i, j in zip(Lstart, Lend):
            if i < j:
                return False
            
        # check R positions are correct
        for i, j in zip(Rstart, Rend):
            if i > j:
                return False
            
        return True