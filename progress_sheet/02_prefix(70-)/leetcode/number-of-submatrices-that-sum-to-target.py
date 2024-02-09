class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix[0])
        m = len(matrix)
        mat = matrix
        for r in range(m):
            for c in range(1, n): 
                mat[r][c] += mat[r][c-1]
            mat[r] += [0]

        ans = 0

        for k in range(n):
            for c in range(k, n):
                preSum = defaultdict(int)
                preSum[0] = 1
                pre = 0
                for r in range(m):
                    pre += mat[r][c] - mat[r][k-1]
                    if pre - target in preSum:
                        ans += preSum[pre-target]
                    preSum[pre] += 1
        for row in mat:
            print(row)
       
        return ans