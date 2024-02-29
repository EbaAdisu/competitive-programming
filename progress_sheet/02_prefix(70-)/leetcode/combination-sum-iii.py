class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def isValid(li,ans ):
            if len(li) != k:return False
            if sum(li) != n: return False
            if li in ans: return False
            return True
        nums = [i for i in range(1,10)]
        # print(nums,n)
        ans = []
        def combSum(i,li):
            if i == 9:
                if isValid(li,ans):
                    ans.append(li[:])
                return
            if sum(li) > n:return
            li.append(nums[i])
            combSum(i+1,li)
            li.pop()
            combSum(i+1,li)
        combSum(0,[])
        return ans
        