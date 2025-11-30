class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        candidates = nums[0]
        sets = [set(num) for num in nums[1:]]
        answer = []
        """
        for this logic:
    
        for candidate in candidates:
            for hashset in sets:
                if candidate not in hashset:
                    jump to next candidate

        two ways to do it:
        1. use a flag
        for candidate in candidates:
            valid = True

            for hashset in sets:
                if candidate not in hashset:
                    valid = False
                    break

            if not valid:
                continue   # skip candidate

            # Otherwise do work here
            print("use candidate:", candidate)

        2. use keyword all:
        """
        for candidate in candidates:
            if not all(candidate in hashset for hashset in sets):
                continue
            answer.append(candidate)
        return sorted(answer)