class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strtoint(num):
            n=0
            for e in num:
                t=0
                for i in range(10):
                    if str(i)==e:
                        t=i
                        break
                n=n*10+t
            return n
        def inttostr(n):
            if n==0:return "0"
            s=""
            while n:
                s+=str(n%10)
                n//=10
            return s[::-1]
        ans=strtoint(num1)*strtoint(num2)
        return inttostr(ans )
