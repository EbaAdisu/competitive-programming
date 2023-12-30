class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0 for i in range(n)] for _ in range(m)]
        for r, c in walls:
            mat[r][c] = 3
        for r, c in guards:
            mat[r][c] = 1
        t = len(walls) + len(guards)

        def move(r,c):
            t = 0
            # move up
            ur = r - 1
            while ur >= 0:
                if mat[ur][c] in (1,3):
                    break
                elif mat[ur][c] == 0:
                    t += 1
                    mat[ur][c] = 2
                ur -= 1
                    
            # move down
            dr = r + 1
            while dr < m:
                if mat[dr][c] in (1,3):
                    break
                elif mat[dr][c] == 0:
                    t += 1
                    mat[dr][c] = 2
                dr += 1
            # move right
            rc = c + 1
            while rc < n:
                if mat[r][rc] in (1,3):
                    break
                elif mat[r][rc] == 0:
                    t += 1
                    mat[r][rc] = 2
                rc += 1
            # move left
            lc = c - 1
            while lc >= 0:
                if mat[r][lc] in (1,3):
                    break
                elif mat[r][lc] == 0:
                    t += 1
                    mat[r][lc] = 2
                lc -= 1
            return t
   
        for r, c in guards:
            t += move(r,c)
    
        return m * n - t