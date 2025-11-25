class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        result = []
        
        def backtrack(index):
            # If we've consumed the whole string and have >= 3 numbers
            if index == len(num) and len(result) >= 3:
                return True
            
            # Try all possible next numbers
            current = 0
            for i in range(index, len(num)):
                
                # Leading zero invalid unless it's just "0"
                if i > index and num[index] == '0':
                    break
                
                current = current * 10 + int(num[i])
                
                # Overflow check
                if current > 2**31 - 1:
                    break
                
                # If we have less than 2 numbers, we can just append
                if len(result) < 2:
                    result.append(current)
                    if backtrack(i + 1):
                        return True
                    result.pop()
                else:
                    # Check Fibonacci condition
                    target = result[-1] + result[-2]
                    if current < target:
                        continue
                    elif current > target:
                        break
                    else:
                        # current == target
                        result.append(current)
                        if backtrack(i + 1):
                            return True
                        result.pop()
            
            return False
        
        backtrack(0)
        return result
