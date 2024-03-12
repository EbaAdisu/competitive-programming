class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        seen = set(forbidden)
        l = 0
        ans = 0
        for r, e in enumerate(word):
            ind = r
            while ind >= l and ind > r - 10:
                if word[ind: r+1] in seen:
                    l = ind + 1
                    break
                ind -= 1
            ans = max(r-l+1,ans)
        return ans

