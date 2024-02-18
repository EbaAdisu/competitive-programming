class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i, e in enumerate(s):
            if e == '(':
                stack += [e]
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack += [1]
                else:
                    total = 0
                    while stack[-1] != '(':
                        total += 2*stack.pop()
                    stack.pop()
                    stack += [total]
        return sum(stack)

        