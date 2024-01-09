class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        diag = defaultdict(list)

        for r in range(m):
            for c in range(n): 
                diag[r+c] += [mat[r][c]]

        ans = []
        for k in diag:
            if k % 2:
                ans += diag[k]
            else:
                ans += diag[k][::-1]
        
        return ans