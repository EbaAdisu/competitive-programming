class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        right = sum(nums)
        left = 0
        ans = [0]
        high = right
        for i,e in enumerate(nums):
            if e == 0:
                left += 1
            else:
                right -= 1

            if right + left > high:
                ans = [i+1]
                high = right + left
            elif right + left == high:
                ans += [i+1]
        return ans
