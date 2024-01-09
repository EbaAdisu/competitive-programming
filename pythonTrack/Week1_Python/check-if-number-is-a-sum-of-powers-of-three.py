class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        t=0
        while 3**(t+1)<=n:
            t+=1
        su=3**t
        t-=1
        while t>=0:
            if su+3**t<=n:
                su+=3**t
            if su==n:
                return True 
            t-=1
        return su==n