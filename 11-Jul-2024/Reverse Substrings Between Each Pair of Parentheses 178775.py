# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for e in s:
            if e!=")":
                stack+=[e]
                continue 
            temp_s=[]
            while stack[-1]!="(":
                temp_s=temp_s+[stack.pop()]
            stack.pop()
            stack+=temp_s
        return "".join(stack)
        