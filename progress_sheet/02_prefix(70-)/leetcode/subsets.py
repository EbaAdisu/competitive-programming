class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets(ind,li,nums,ans):
            print(li)
            if ind == len(nums):
                # if li:
                ans.append(li[:])
                return
            li.append(nums[ind])
            subsets(ind+1,li,nums,ans)
            li.pop()
            subsets(ind+1,li,nums,ans)
            return ans
        return subsets(0,[],nums,[])