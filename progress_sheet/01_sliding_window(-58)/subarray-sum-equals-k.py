class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dupi = defaultdict(int)
        dupi[0] = 1
        pre = 0
        ans = 0
        for e in nums:
            pre += e
            if pre - k in dupi:
                ans += dupi[pre-k]
            dupi[pre] += 1
        return ans



        