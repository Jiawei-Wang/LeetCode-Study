class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        stack = deque([nums2[0]])
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                element = stack.pop()
                hashmap[element] = nums2[i]
            stack.append(nums2[i])
        answer = []
        for target in nums1:
            if target in hashmap:
                answer.append(hashmap[target])
            else:
                answer.append(-1)
        return answer
