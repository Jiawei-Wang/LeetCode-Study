class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1 = students.count(1)
        s0 = students.count(0)
        for sand in sandwiches:
            if sand and s1:
                s1 -= 1
            elif not sand and s0:
                s0 -= 1
            else:
                break
        return s1 + s0