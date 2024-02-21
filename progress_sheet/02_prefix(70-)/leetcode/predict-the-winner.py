class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(l,r,total,turn):
            if l == r:
                return total + nums[l] >= 0
            total += nums[l] if turn else -nums[l]
            choice1 = winner(l+1,r,total, 1-turn )
            total -= nums[l] if turn else -nums[l]
            total += nums[r] if turn else -nums[r]
            choice2 = winner(l,r-1,total,1-turn)
            if turn:
                return choice1 or choice2
            else:
                return choice1 and choice2
        return  winner(0,len(nums)-1,0,1)