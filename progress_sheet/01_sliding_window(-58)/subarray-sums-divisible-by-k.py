class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashu = defaultdict(int)
        hashu[0] = 1
        pre = 0
        ans = 0
        for e in nums:
            pre += e
            ans += hashu[pre%k]
            hashu[pre%k]+=1
        return ans

        