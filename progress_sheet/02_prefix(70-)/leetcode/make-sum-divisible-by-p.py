class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        post = defaultdict(list)
        post[0] = [n]
        pos = 0
        for i in range(n-1,-1,-1):
            pos += nums[i]
            post[pos%p] += [i]
        pre = 0
        ans = n
        if pre in post:
            ans = post[0][-1]
        for r in range(n):
            pre += nums[r]
            rem = -pre%p
            if rem in post:
                while post[rem] and post[rem][-1] <= r:
                    post[rem].pop()
                if post[rem]:
                    ans = min(ans,post[-pre%p][-1] - r -1)
                else:
                    post.pop(rem)
    
        if ans == n: return -1
        return ans