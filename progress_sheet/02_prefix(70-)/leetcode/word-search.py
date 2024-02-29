class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def backtrack(path,r,c):
            if len(path) == len(word):
                return True
            if c == n:
                if not path:
                    if backtrack(path,r+1,0): return True
                return 
            if r == m:return
            if not path:
                if board[r][c] == word[0]:
                    path += [(r,c)]
                    if backtrack(path,r,c): return True
                    path.pop()
                if backtrack(path,r,c+1): return True
            else:
                if c + 1 < n:
                    if (r,c+1) not in path and board[r][c+1] == word[len(path)]:
                        path += [(r,c+1)]
                        if backtrack(path,r,c+1): return True
                        path.pop()
                if c - 1 >= 0:
                    if (r,c-1) not in path and board[r][c-1] == word[len(path)]:
                        path += [(r,c-1)]
                        if backtrack(path,r,c-1): return True
                        path.pop()
                if r + 1 < m:
                    if (r+1,c) not in path and board[r+1][c] == word[len(path)]:
                        path += [(r+1,c)]
                        if backtrack(path,r+1,c): return True
                        path.pop()
                if r - 1 >= 0:
                    if (r-1,c) not in path and board[r-1][c] == word[len(path)]:
                        path += [(r-1,c)]
                        if backtrack(path,r-1,c): return True
                        path.pop()
            return False

        return backtrack([],0,0)

                