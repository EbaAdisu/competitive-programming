class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[0]*len(s)
        for index in range(len(s)):
            ans[indices[index]]=s[index]
        return ''.join(ans)