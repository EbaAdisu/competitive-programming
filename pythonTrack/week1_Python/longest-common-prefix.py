class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=strs[0]
        for e in strs:
            mi=min(len(pre ),len(e))
            for i in range(min(len(pre),len(e))):
                if e[i]!=pre[i]:
                    pre=pre[:i]
                    break
            else:
                pre=pre[:mi]
        return pre 
