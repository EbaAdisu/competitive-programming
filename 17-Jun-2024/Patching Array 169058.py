# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        pre = 0
        ans = 0
        past = 0
        for e in nums:
            if e > n:
                break
            while pre < e:
                if pre + 1 == e:
                    break
                pre += pre + 1
                ans += 1
            pre += e
            past = e
            # print(e, ans, pre, past)
        while pre < n:
            pre += pre + 1
            ans += 1
        return ans