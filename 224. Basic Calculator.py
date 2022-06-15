# 在之前（没有括号存在的中缀运算式）基础上添加了括号，但是删去了乘法和除法
# 1. 因为没有乘法和除法，所以对于每个数字而言，只要关注它是正还是负即可，运算顺序并不重要
# 2. 对于空格的处理：我们可以直接略过它
class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        i, signs = 0, [1, 1] # 'i' for current string index, 'signs' for the overall sign of each number
        while i < len(s): # iterate over the string
            c = s[i]
            if c.isdigit(): # real work here, for each number encountered in the string
                start = i # the number can be multi-digit, so store starting index
                while i < len(s) and s[i].isdigit(): # find the ending index(plus one) of current number in the string
                    i += 1
                total += signs.pop() * int(s[start:i]) # now we have the number, and the sign of the number, just add it to total
                continue
            if c in '+-(': # push signs for ensuing number
                signs += signs[-1] * (1, -1)[c == '-'], # look at the last sign and use multiplication to calculate the overall sign ( just as in what you will do when trying to eliminate parentheses in arithmetic formulas (flatten the formulas).
            elif c == ')': # pop signs to reflect current overall sign
                signs.pop()
            i += 1 # increment the counter
        return total

    """    
    In line signs += signs[-1] * (1, -1)[c == '-'],
    notice that in the end there is a comma, this is required as to transform the right hand side operand to single-value tuple. 
    So this line is actually signs.extend(( signs[-1] * (1, -1)[c == '-'],)).
    https://stackoverflow.com/questions/39732771/what-is-the-usage-of-comma-in-augmented-list-assignment
    """
    
    """
    TODO: 上面答案没看明白，还要再看
    """