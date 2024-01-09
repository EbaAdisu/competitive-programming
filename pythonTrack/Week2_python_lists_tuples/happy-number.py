class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set([n])
        while n!=1:
            num=0
            n=str(n)
            for e in n:
                num+=int(e)**2
            n=num
            if n in seen:
                return False
            seen.add(n)
        return True