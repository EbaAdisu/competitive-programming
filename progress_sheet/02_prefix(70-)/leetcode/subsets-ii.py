class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subsets(ind,li,nums,ans):
            # print(li)
            if ind == len(nums):
                # print(li)
                if li:
                    nli = sorted(li)
                    if nli not in ans:
                        ans.append(nli[:])
                return
            li.append(nums[ind])
            subsets(ind+1,li,nums,ans)
            li.pop()
            subsets(ind+1,li,nums,ans)
            return ans
        return subsets(0,[],nums,[[]])