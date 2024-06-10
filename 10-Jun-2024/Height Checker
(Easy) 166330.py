# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        answer = 0
        for ind in range(len(heights)):
            if heights[ind] != expected[ind]:
                answer += 1
        return answer
        