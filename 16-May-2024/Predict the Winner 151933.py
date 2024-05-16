# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        cache = {}
        def game(l,r,turn):
            if l > r:
                return 0
            if (l,r, turn ) in cache:
                return cache[(l,r,turn)] 
            left = -game(l+1, r, 1- turn) + nums[l]
            right = -game(l, r -1, 1-turn) + nums[r]
            cache[(l,r,turn)] = max(left,right)
            return cache[(l,r,turn)] 
        return game(0,len(nums)-1,0) >= 0