class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        for elemetns on the same diagonal, they have the same (sum of indexes)
        for example:
            1  2  3  4
            5  6  7  8 
            9  10 11 12
            13 14 15 16
        2 has [0, 1] and 5 has [1, 0]
        4 has [0, 3] and 13 has [3, 0]
        so we can group ones with same index sum first
        """
        d = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
                    d[i+j].append(matrix[i][j])
        """
        elements in d are ordered, use the same example above,
        d = {0: [1], 
             1: [2, 5], 
             2: [3, 6, 9], 
             3: [4, 7, 10, 13], 
             4: [8, 12, 14], 
             5: [12, 15], 
             6: [16]}
        the diagonal is always from top right to bottom left
        """
        
        # then we use the dictionary to build answer
        ans = []
        for diagonal in d.items():
            if diagonal[0] % 2 == 0:
				# Here we append in reverse order because its an even numbered level/diagonal. 
                for x in diagonal[1][::-1]:
                    ans.append(x)
            else:
                for x in diagonal[1]:
                    ans.append(x)
        return ans
                

