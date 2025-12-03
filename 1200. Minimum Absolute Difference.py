class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        answer = []
        diff = float("inf")
        for i in range(len(arr)-1):
            curr = arr[i+1] - arr[i]
            if curr < diff:
                answer = [[arr[i], arr[i+1]]]
                diff = curr
            elif curr == diff:
                answer.append([arr[i], arr[i+1]])
            else:
                continue
        return answer
        