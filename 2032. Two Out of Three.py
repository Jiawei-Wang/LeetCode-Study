class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        target = set1.union(set2.union(set3))
        
        def count(ele):
            count = 0
            if ele in set1:
                count += 1
            if ele in set2:
                count += 1
            if ele in set3:
                count += 1
            return count
        
        ans = []
        
        for ele in target:
            if count(ele) >= 2:
                ans.append(ele)
        
        return ans
        

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = list(set(nums1))+list(set(nums2))+list(set(nums3))
        dic = Counter(nums)
        res = []
        for k,v in dic.items():
            if v >= 2:
                res.append(k)
        return res