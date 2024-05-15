# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i,pali,ans):
            if i == len(s):
                ans += [pali[:]]
                return
            for j in range(i,len(s)):
                e = s[i:j+1]
                if e == e[::-1]:
                    pali.append(e)
                    backtrack(j+1,pali,ans)
                    pali.pop()
            return ans
        return backtrack(0,[],[])

            