# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def game(l,r,turn):
            if l > r:
                return 0
            if (l,r, turn ) in cache:
                return cache[(l,r,turn)] 
            left = -game(l+1, r, 1- turn) + piles[l]
            right = -game(l, r -1, 1-turn) + piles[r]
            cache[(l,r,turn)] = max(left,right)
            return cache[(l,r,turn)] 
        return game(0,len(piles)-1,0) > 0

        