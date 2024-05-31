# return length of the longest subarray with only 2 values
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        answer = 0
        two = dict()
        while right < len(fruits):
            fruit = fruits[right]

            if right == len(fruits) - 1:
                if fruit in two or len(two) < 2:
                    answer = max(answer, right-left+1)
                else:
                    answer = max(answer, right - left)
                break

            if fruit in two:
                two[fruit] += 1
                right += 1
                continue
            else:
                if len(two) == 2:
                    answer = max(answer, right-left)
                    while len(two) == 2:
                        two[fruits[left]] -= 1
                        if two[fruits[left]] == 0:
                            del two[fruits[left]]
                        left += 1
                    continue    
                else:
                    two[fruit] = 1
                    right += 1
                    continue
        
        return answer

