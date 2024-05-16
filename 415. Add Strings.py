class Solution:
    def addStrings(self, nums1: str, nums2: str) -> str:
        if len(nums1) < len(nums2):
            n1 = nums1[::-1]
            n2 = nums2[::-1]
        else:
            n1 = nums2[::-1]
            n2 = nums1[::-1]

        n3 = [0] * len(n2) 
        carry = 0    

        for i in range(len(n1)):
            d1 = int(n1[i])
            d2 = int(n2[i])
            result = (d1+d2+carry) % 10
            carry = (d1+d2+carry) // 10
            n3[i] = result
        
        for j in range(len(n1), len(n2)):
            d2 = int(n2[j])
            result = (d2+carry) % 10
            carry = (d2 + carry) // 10
            n3[j] = result
        
        if not carry:
            return "".join(str(x) for x in n3[::-1])
        else:
            return "1" + "".join(str(x) for x in n3[::-1])