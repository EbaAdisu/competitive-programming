class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(li,coll,ans):
            if not coll:
                ans.append(li[:])
                return
            for i in range(len(coll)):
                li.append(coll[i])
                perm(li,coll[:i]+coll[i+1:],ans)
                li.pop()
            return ans
        return perm([],nums,[])