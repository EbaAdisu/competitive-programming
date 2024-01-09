class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat )
        diag1 = 0
        diag2 = 0
        for r in range(n):
            for c in range(n):
                if r + c == n - 1:
                    diag2 += mat[r][c]
                elif r - c == 0:
                    diag1 += mat[r][c]
        return diag1 + diag2 