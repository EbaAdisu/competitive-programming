class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix[0])
        m = len(matrix)
        mat = matrix
        for r in range(m):
            for c in range(n):
                total = 0
                if c > 0:
                    total += mat[r][c-1]
                if r > 0:
                    total += mat[r-1][c]
                if c > 0 and r > 0:
                    total -= mat[r-1][c-1] 
                mat[r][c] += total 
        self.mat = mat
        for row in mat:
            print(row)
        # print(selt.mat)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.mat[row2][col2]
        if col1 > 0:
            total -= self.mat[row2][col1-1]
        if row1 > 0:
            total -= self.mat[row1 -1][col2]
        if row1 > 0  and col1 > 0 :
            total += self.mat[row1-1][col1-1]
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)