# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def inbound(r,c):
            if 0<=r<m and 0<=c<n:
                return mat[r][c]
            return 0
        m, n = len(matrix), len(matrix[0])
        mat1 = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                if c == 0:
                    if matrix[r][c] == '1':
                        mat1[r][c] += 1
                elif matrix[r][c] == '1':
                    mat1[r][c] += mat1[r][c-1] + 1
        #     print(mat1[r])
        # print()
        mat2 = [[0]*n for i in range(m)]
        for c in range(n):
            for r in range(m):
                if r == 0:
                    if matrix[r][c] == '1':
                        mat2[r][c] += 1
                elif matrix[r][c] == '1':
                    mat2[r][c] += mat2[r-1][c] + 1
        # for row in mat2:
        #     print(row)
        # print()

        ans = 0
        mat = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                if matrix[r][c]:
                    mat[r][c] = min(inbound(r-1,c-1) + 1, mat1[r][c], mat2[r][c])
                ans = max(mat[r][c], ans)
            # print(mat[r])
        return ans ** 2