# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        m = len(matrix)
        for r in range(1,m):
            for c in range(n):
                mini = min(matrix[r-1][max(0,c-1):min(n,c+2)])
                matrix[r][c] += mini
                
        return min(matrix[-1])
