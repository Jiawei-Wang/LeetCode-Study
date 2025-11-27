class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = defaultdict(int)
        max_score = 0
        i = len(questions) - 1
        while i >= 0:
            point, brainpower = questions[i]
            # two choices: skip this question or do this question
            dp[i] = max(max_score, point + dp[i+brainpower+1])
            max_score = max(max_score, dp[i])
            i -= 1
        return max_score
