class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        k = len(p)
        window = Counter(s[:k])
        ans = []

        for i in range(len(s) - k):

            if window == count:
                ans += [i]

            window[s[i]] -= 1
            window[s[i+k]] += 1
            
            # if window[s[i]] == 0:
            #     del window[s[i]]
        
        if window == count:
            ans +=[len(s)-k]

        return ans
