class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list)
        ans = 0
        for i, e in enumerate(nums):
            if e in pos:
                for j in pos[e]:
                    if (j * i) % k == 0:
                        ans += 1
            pos[e] += [i]
            
        return ans
            