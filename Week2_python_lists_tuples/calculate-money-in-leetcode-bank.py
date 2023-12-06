class Solution:
    def totalMoney(self, n: int) -> int:
        rem=n%7
        que=n//7
        ans=0
        week=0
        cw=28
        while week<que:
            ans+=cw
            cw+=7
            week+=1
        day=0
        cd=que+1
        while day<rem:
            ans+=cd
            cd+=1
            day+=1
        return ans