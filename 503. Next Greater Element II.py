class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        twiceLongNums = [element for element in nums] * 2
        answer = [-1] * len(twiceLongNums)
        stack = []
        for longIndex, longElement in enumerate(twiceLongNums):
            while stack and stack[-1][1] < longElement:
                answer[stack.pop()[0]] = longElement
            stack.append((longIndex, longElement))
        return answer[0: len(twiceLongNums)//2]
        

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = []
        
        for i in range(2 * n): # Loop through the elements twice to save space
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                answer[stack.pop()] = nums[index]
            if i < n:
                stack.append(i) # once store elements in the first loop to skip some calculations
        
        return answer