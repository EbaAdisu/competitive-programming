class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        nums = sorted(deck)
        ans = deque()
        ans.append(nums.pop())
        while nums:
            ans.appendleft(ans.pop())
            ans.appendleft(nums.pop())
        return ans
        