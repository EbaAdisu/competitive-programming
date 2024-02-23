class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ele in s:
            if ele == ']':
                encodedString = ''
                while stack[-1]!='[':
                    encodedString += stack.pop()
                stack.pop()
                multiple = ''
                while stack and stack[-1] in '0123456789':
                    multiple += stack.pop()
                stack += list(encodedString[::-1])*int(multiple[::-1])
            else:
                stack += [ele]
        return ''.join(stack)
                    
        