class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i, e in enumerate(s):
            if e == '(':
                stack += [e]
            else:
                stack.pop()
                if s[i-1] == '(':
                    ans += 2**len(stack)
        return ans

        