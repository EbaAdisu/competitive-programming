class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(para):
            op = 0
            for e in para:
                if e == '(':
                    op += 1
                else:
                    op -= 1
                if op < 0: return -1
            return op
        def backtrack(para,ans):
            if len(para) == n*2:
                if isValid(para) == 0:
                    ans += [para]
                return
            if 0 <= isValid(para + '(') <= n:
                backtrack(para+'(',ans)
            if 0 <= isValid(para + ')') <= n:
                backtrack(para+')',ans)
            return ans
        ans = backtrack('',[])
        # print(ans)
        return ans
        