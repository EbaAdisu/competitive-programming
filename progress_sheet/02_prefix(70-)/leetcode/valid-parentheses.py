class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','{':'}','[':']'}
        li=[]
        for i in s:
            if i in dic:
                li.append(i)
            elif len(li) and dic[li[-1]]==i:
                li.pop()
            else:return False
        return len(li)==0
                