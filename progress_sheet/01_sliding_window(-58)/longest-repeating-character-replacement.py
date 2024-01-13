class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        l = 0
        ans = 0

        for r, e in enumerate(s):
            count[e]+=1
            while r-l+1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans