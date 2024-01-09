class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        # the row
        for i in range(1, n-1):
            base=matrix[0][i]
            t=1
            while t<m and  t+i <n:
                if matrix[t][i+t]!=base:
                    return False
                t+=1
        # the coloumn
        for i in range(1,m-1):
            base=matrix[i][0]
            t=1
            while t<n and t+i<m:
                if matrix[i+t][t]!=base:
                    return False
                t+=1
        # diagonal
        base=matrix[0][0]
        t=1
        while t<m and t<n:
            if matrix[t][t]!=base:
                return False
            t+=1
        return True

        
