class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        t = n
        def backtrack(t,li,ans):
            if t > n: 
                return
            if len(li) == k:
                ans += [li[:]]
                return
            t+=1
            li.append(t)
            backtrack(t,li,ans)
            li.pop()
            backtrack(t,li,ans)
            return ans
        return backtrack(0,[],[])