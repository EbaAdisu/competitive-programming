class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(l,r,score,turn):
            if l == r:
                return score + nums[l] >= 0
            score += nums[l] if turn else -nums[l]
            takeleft = winner(l+1,r,score, 1-turn )

            score -= nums[l] if turn else -nums[l]
            score += nums[r] if turn else -nums[r]
            takeright = winner(l,r-1,score,1-turn)
            
            if turn:
                return takeleft or takeright
            else:
                return takeleft and takeright
        return  winner(0,len(nums)-1,0,1)