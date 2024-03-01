class Solution:
    def totalNQueens(self, n: int) -> int:
        def validPos(board,r,c):
            # # left
            # rc = c + 1
            # while rc < n:
            #     if board[r][rc]:return False
            #     rc += 1
            # # right
            # lc = c - 1
            # while lc >= 0:
            #     if board[r][lc]:return False
            #     lc -= 1
            # up
            ur = r - 1
            while ur >= 0:
                if board[ur][c]:return False
                ur -= 1 
            # down
            dr = r + 1
            while dr < n:
                if board[dr][c]:return False
                dr += 1
            # up left
            ulr = r - 1
            ulc = c + 1
            while ulr >= 0 and ulc < n:
                if board[ulr][ulc]:return False
                ulr -= 1
                ulc += 1
            # up right
            urr = r - 1
            urc = c - 1
            while urr >= 0 and urc >= 0:
                if board[urr][urc]:return False
                urr -= 1
                urc -= 1
            # down left
            dlr = r + 1
            dlc = c + 1
            while dlr < n and dlc < n:
                if board[dlr][dlc]:return False
                dlr += 1
                dlc += 1
            # down right
            drr = r + 1
            drc = c - 1
            while drr < n and drc >= 0:
                if board[drr][drc]:return False
                drr += 1
                drc -= 1
            # print(r,c)
            return True
        

        
        board = [[0]*n for i in range(n)]
        ans = []
        def putQueen(board,r,c):
            if r == n:
                if sum([sum(li) for li in board]) == n:
                    ans.append(1)
                return
            if r > n or sum([sum(li) for li in board]) > n:
                return
            if validPos(board,r,c):
                board[r][c] = 1
                putQueen(board,r+1,0)
            board[r][c] = 0
            if c +1 < n and sum(board[r]) == 0:
                putQueen(board,r,c+1)
        putQueen(board,0,0)
        
        return len(ans)