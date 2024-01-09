class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        pos=0
        for i in range(len(s)):
            if pos<len(spaces) and i == spaces[pos]:
                pos+=1
                ans+=" "
            ans+=s[i]
        return ans 