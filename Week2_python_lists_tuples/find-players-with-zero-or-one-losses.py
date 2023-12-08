class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=defaultdict(int)
        los=defaultdict(int)
        for w,l in matches:
            win[w]+=1
            los[l]+=1
        ans=[[],[]]
        for w in win:
            if los[w]==0:
                ans[0]+=[w]
        ans[0].sort()
        for l in los:
            if los[l]==1:
                ans[1]+=[l]
        ans[1].sort()
        return ans 