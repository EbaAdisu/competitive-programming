# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def inbound(r,c):
            if 0<=r<m and 0<=c<n:
                return mat[r][c]
            return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0
        mat = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    mat[r][c] = min(inbound(r-1, c-1) + 1, inbound(r-1, c) + 1, inbound(r,c-1) + 1)
                ans = max(mat[r][c], ans)
            # print(mat[r])
        return ans ** 2