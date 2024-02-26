class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(t,li,ans):
            if sum(li) == target:
                if li not in ans:
                    ans += [li[:]]
                return
            if sum(li) > target:
                return
            if t == len(candidates): 
                return
            li.append(candidates[t])
            backtrack(t,li,ans)
            backtrack(t+1,li,ans)
            li.pop()
            # backtrack(t,li,ans)
            backtrack(t+1,li,ans)
            return ans
        return backtrack(0,[],[])