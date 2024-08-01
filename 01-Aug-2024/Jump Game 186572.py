# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i, e in enumerate(nums):
            curr = max(e,curr)
            if curr == 0 and i != len(nums)-1:
                return False
            if i + curr >= len(nums)-1:
                return True
            curr -= 1
        