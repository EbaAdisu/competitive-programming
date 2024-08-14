# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        odd = [e for e in nums if e > 0]
        even = [e for e in nums if e < 0]
        ans = []
        for i in range(len(odd)):
            ans.extend([odd[i],even[i]])
        return ans
        