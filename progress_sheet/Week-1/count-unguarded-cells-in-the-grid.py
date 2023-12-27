class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0 for i in range(n)] for _ in range(m)]
        guards = set([tuple(g) for g in guards])
        walls = set([tuple(w) for w in walls])
        t = 0

        def move(r,c):
            t = 0
            # move up
            ur = r - 1
            while ur >= 0:
                if (ur,c) in walls or (ur,c) in guards:
                    break
                if mat[ur][c] == 0:
                    t += 1
                    mat[ur][c] = 2
                ur -= 1
                    
            # move down
            dr = r + 1
            while dr < m:
                if (dr,c) in walls or (dr,c) in guards:
                    break
                if mat[dr][c] == 0:
                    t += 1
                    mat[dr][c] = 2
                dr += 1
            # move right
            rc = c + 1
            while rc < n:
                if (r,rc) in walls or (r,rc) in guards:
                    break
                if mat[r][rc] == 0:
                    t += 1
                    mat[r][rc] = 2
                rc += 1
            # move left
            lc = c - 1
            while lc >= 0:
                if (r,lc) in walls or (r,lc) in guards:
                    break
                if mat[r][lc] == 0:
                    t += 1
                    mat[r][lc] = 2
                lc -= 1
            return t
   
        for r, c in guards:
            t += move(r,c)
    
        return m * n - t - len(guards) - len(walls)