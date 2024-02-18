class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid=set(["+","-","*","/"])
        cal=[]
        for i in tokens:
            if i not in valid:
                cal.append(i)
            elif i=='+':
                x=int(cal.pop())
                y=int(cal.pop())
                cal.append(x+y)
            elif i=='-':
                x=int(cal.pop())
                y=int(cal.pop())
                cal.append(y-x)
            elif i=='*':
                x=int(cal.pop())
                y=int(cal.pop())
                cal.append(x*y)
            elif i=='/':
                x=int(cal.pop())
                y=int(cal.pop())
                cal.append(int(y/x))
        return int(cal[0])