class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        for i in range(0, len(s), k):
            curr = s[i: i+k]
            if len(curr) != k:
                curr += fill * (k-len(curr))
            answer.append(curr)
        return answer