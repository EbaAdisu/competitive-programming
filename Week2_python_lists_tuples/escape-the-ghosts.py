class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_dis=abs(target[0])+abs(target[1])
        for x,y in ghosts:
            g_dis=abs(x-target[0])+abs(y-target[1])
            if g_dis<=my_dis:
                return False
        return True