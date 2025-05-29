class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [p[0] for p in sorted(zip(names, heights), key=lambda person: -person[1])]

        """
        1. zip(names, heights): two lists into pairs
        2. sorted(..., key=lambda person: -person[1]): 
                person: the zipped tuple
                sort in descending way using height
        3. return the name list
        """