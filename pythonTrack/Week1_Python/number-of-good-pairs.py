class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for k in count:
            for i in range(count[k]):
                ans+=i
        return ans