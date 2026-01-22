class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        answer = []
        while counter:
            current = []
            # hashmap can't be modified during traversal
            for key in list(counter.keys()):  # so a snapshot is needed
                current.append(key)
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]
            answer.append(current)

        return answer
