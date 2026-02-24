class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        answer = []
        index1 = 0
        index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            curr1 = nums1[index1]
            curr2 = nums2[index2]
            if curr1[0] < curr2[0]:
                answer.append(curr1)
                index1 += 1
            elif curr1[0] > curr2[0]:
                answer.append(curr2)
                index2 += 1
            else:
                answer.append([curr1[0], curr1[1]+curr2[1]])
                index1 += 1
                index2 += 1
        
        if index1 == len(nums1):
            answer.extend(nums2[index2:])
        elif index2 == len(nums2):
            answer.extend(nums1[index1:])
        return answer