# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]* n
        for i in range(n-1,-1,-1):
            pick = questions[i][0]
            if i + questions[i][1] + 1 < n:
                pick += dp[i + questions[i][1] + 1]
            not_pick = 0
            if i + 1 < n:
                not_pick += dp[i+1]
            dp[i] = max(pick,not_pick)
        return dp[0]
            
        