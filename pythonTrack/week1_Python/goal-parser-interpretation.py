class Solution:
    def interpret(self, command: str) -> str:
        stack=[]
        s=''
        for e in command:
            if e==')':
                if len(stack)==1:
                    s+="o"
                else:
                    s+="al"
                stack=[]
            elif e=="G":
                s+=e
            else:
                stack+=[e]
        return s