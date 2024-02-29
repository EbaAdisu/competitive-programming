class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse = True)
        count = Counter(candidates)
        for key in count:
            while count[key] * key > target:
                candidates.remove(key)
                count[key] -= 1
        presum = candidates[::-1]
        for i in range(1,len(presum)):
            presum[i] += presum[i-1]
        presum = presum[::-1]
        def backtrack(t,li,ans):
            if sum(li) == target:
                if li not in ans:
                    ans += [li[:]]
                return
            if sum(li) > target:
                return
            if t == len(candidates): 
                return
            if presum[t] + sum(li) < target: 
                return

            li.append(candidates[t])
            backtrack(t+1,li,ans)
            li.pop()
            backtrack(t+1,li,ans)
            return ans
        return backtrack(0,[],[])