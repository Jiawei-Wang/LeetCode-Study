class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        def backtrack(i, path, resultSoFar, prevNum):
            # i: index of current location on input string
            # path: output string
            # resultSoFar: calculation result of path
            """
            prevNum: result of last number
            explain:
            1. if a "*" happens, resultSoFar needs to be update first (by deducting the previous one)
            2. then the new number needs to be combined with the previous one
            example: 
            a + b * c: resultSofar = a + b, and it needs to be back to a, then add b * c
            """

            # if we have visited all posible locations, we need to return (regardless if we got to target)
            if i == len(s):
                if resultSoFar == target: 
                    ans.append(path)
                return 

            # for current number, we need to decide how long the number should be
            for j in range(i, len(s)): # it can be of any length available
                
                if s[i] == '0' and j > i: # but if it has leading zero, we don't have to continue 
                    break 

                num = int(s[i:j + 1])
                
                # for this new number: num
                if i == 0: # if it is the first number
                    # index for next loop will be the location after first number
                    # path will be just the string version of first number
                    # resultSoFar will be just the first number (we can only add)
                    # prevNum will be just the first number
                    backtrack(j + 1, path + str(num), resultSoFar + num, num)  

                else: # if it is not the first number 
                    # index will be the same: location after this number
                    # then we have 3 possible operations
                    backtrack(j + 1, path + "+" + str(num), resultSoFar + num, num)
                    backtrack(j + 1, path + "-" + str(num), resultSoFar - num, -num)
                    backtrack(j + 1, path + "*" + str(num), resultSoFar - prevNum + prevNum * num, prevNum * num)  
                    # "*" means we need to remove calculation happened in the last step first then redo it
                    # example: 1+2*3*4: 
                    # 2 was added last step, so it will be deducted first, then 2*3 will be added
                    # same thing for 2*3: 2*3 will be deducte first, then 2*3*4 will be added

        ans = []
        backtrack(0, "", 0, 0)
        return ans