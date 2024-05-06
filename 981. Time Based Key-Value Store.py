from collections import defaultdict

class TimeMap:

    # initilize key-value store: key = key, value = list 
    def __init__(self):
        self.hashmap = defaultdict(list)

    # put value and timestamp into the list
    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp only increases so the list is always sorted 
        self.hashmap[key].append((timestamp, value))

    # get the last value in the list with timestamp <= target timestamp 
    # target is not guaranteed to be in the list
    # for example: [1, 2, 4]
    # 2 is the last one <= target 2
    # 2 is the last one <= target 3 
    def get(self, key: str, target: int) -> str:
        array = self.hashmap[key]
        length = len(array)

        # the smallest index will be -1 (target < every timestamp)
        # the biggest index will be length - 1 (every timestamp <= target)
        left = 0 
        right = length - 1 

        while left <= right:
            mid = left + (right - left)//2
            timestamp = array[mid][0]
            value = array[mid][1]
            """
            timestamp only increases so every timestamp in the list is different
            if we find target then it's guaranteed to be the unique one
            so we have three conditions instead of two: mid is never carried into next loop
            """
            if timestamp == target:  
                return value
            elif timestamp < target:
                left = mid + 1
            else:
                right = mid - 1

        """
        why left <= right instead of left < right:
        1. mid is not included in the next loop, so subarray that we got rid of is 
           guaranteed to be all < target or all > target 
        2. we don't know where target is in the carried over subarray
        3. if >= 4 elements: same as before

        4. if 3 elements: left + 1 = mid = right - 1, so if mid != target
            1) left becomes right
            2) or right becomes left
            either case: 
                1- for example [4, 6, 8] target 4, right becomes left: in this example (while left < right) works:
                   we know mid 6 > target, we know nothing about left = new right with target
                   loop ends here with left = new right = 4, we return new right, which happens to be correct
                2- for example [4, 6, 8] target 5, right becomes left: in this example (while left < right) still works:
                   we know mid 6 > target, we know nothing about left = new right with target
                   loop ends here with left = new right = 4, we return new right, which happens to be correct
                3- for example [4, 6, 8] target 3, right becomes left: in this example (while left < right) doesn't work:
                   we know mid 6 > target, we know nothing about left = new right with target
                   loop ends here with left = new right = 4, we return new right, which is incorrect    
            (in the above examples the issue is: 
                1) we can only guarantee the element to the left of 4 is smaller than target
                2) we don't know about left = new right 
            this applies to new left = right as well, we only know everything on the right of 8 is bigger than target
            we don't know relationship between new left = right and target
            for example [4, 6, 8] target = 8: (while left < right) works 
            for example [4, 6, 8] target = 9: (while left < right) works 
            for example [4, 6, 8] target = 7: (while left < right) doesn't work)

            so we still need another loop to check relationship between left = right = mid (only 1 element left) and target
                
        5. when only 2 elements left: left = mid = right - 1
            1) mid < target: left becomes right (go into only 1 element left case)
            2) mid > target: right becomes left - 1, loop ends
                             discarded subarray < target < carried over subarray
                             we return index of last element in discarded subarray
        
        6. when only 1 element left: left = mid = right
            1) if mid < target: we already know target < the element on the right side of mid
                                we let left = right + 1, right stays, loop ends, right is the correct answer
            2) if mid > target: we already know the element on the left sie of mid < target
                                we let right = left - 1, loop ends, right is the correct answer
        """

        if right < 0:
            return ""
        else:
            return array[right][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# improve from last answer
class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dic[key]
        n = len(arr)
        
        left = 0
        right = n 

        """
        why right = n not right = n - 1
        because we use right to represent first element that is > target
        so range goes from [-1, n - 1] (included) to [0, n] (included)

        this will turn the question into bisect_right:
        1. everything on the left <= target < everything on the right
        2. return index is where target should be inserted
        3. so the true answer is return index - 1 (last element that <= target)
        """
        
        while left < right:
            """
            why while left < right instead of while left <= right:
            1. mid is not excludded, we allow right = mid
            2. so if mid > timestamp and left = right: we enter endless loop
            """
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1 # target should be at least inserted at mid + 1
            elif arr[mid][0] > timestamp:
                right = mid # target should be at most inserted at mid

        # right is the first element that is > target, everything on the left is <= target
        return "" if right == 0 else arr[right - 1][1]


