class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows 
        for i in range(9):
            row=set()
            for j in range(9):
                if board[i][j]==".":continue 
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
            #col
            col=set()
            for k in range(9):
                if board[k][i]==".":
                    continue
                if board[k][i] in col:
                    return False
                col.add(board[k][i])
        #box
        for i in range(0,9,3):
            for j in range(0,9,3):
                box=set()
                for k in range(3):
                    for c in range(3):
                        if board[i+k][j+c]==".":continue
                        if board[i+k][j+c] in box:return False
                        box.add(board[i+k][j+c])

        return True 
    
