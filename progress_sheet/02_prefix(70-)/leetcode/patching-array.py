class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums += [n]
        pre = 0
        ans = 0
        for e in nums:
            while pre < e:
                if pre + 1 == e:
                    break
                pre += pre + 1
                ans += 1
                if pre > n:
                    return ans
            pre += e
            if pre > n: return ans

        return ans