class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(r,c,val):
            for i in range(9):
                if board[r][i] == val: return False
            for i in range(9):
                if board[i][c] == val: return False
            secr = r//3*3
            secc = c//3*3
            for i in range(secr,secr+3):
                for j in range(secc,secc+3):
                    if board[i][j] == val: return False
            return True
        def solve(r,c):
            if c >= 9:
                return solve(r+1,0) == True
                
            if r == 9: return True
            if board[r][c] != '.':
                return solve(r, c+1)
                
            for i in range(1,10):
                if valid(r,c,str(i)):
                    board[r][c] = str(i)
                    if solve(r, c+1): return True
                    board[r][c] = '.'
            else:
                return False
        solve(0,0)
