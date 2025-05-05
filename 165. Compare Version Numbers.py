class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        if len(v1) < len(v2):
            while len(v1) < len(v2):
                v1.append(0)
        elif len(v2) < len(v1):
            while len(v2) < len(v1):
                v2.append(0)
        
        for i in range(len(v1)):
            n1 = v1[i]
            n2 = v2[i]
            if n1 < n2:
                return -1
            elif n2 < n1:
                return 1
            
        return 0
    

from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))

        for num1, num2 in zip_longest(v1, v2, fillvalue=0):
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        return 0