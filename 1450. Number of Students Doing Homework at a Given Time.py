class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students = zip(startTime, endTime)
        count = 0
        for s, e in students:
            if s <= queryTime <= e:
                count += 1
        return count