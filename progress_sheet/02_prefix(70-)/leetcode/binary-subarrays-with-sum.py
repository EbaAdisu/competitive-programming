class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        save = defaultdict(int)
        save[0] = 1
        ans = pre = 0
        for e in nums:
            pre += e
            if pre - goal in save:
                ans += save[pre-goal]
            save[pre]+=1
        return ans
