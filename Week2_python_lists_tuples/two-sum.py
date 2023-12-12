class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count=defaultdict (int )
        for i,e in enumerate(nums ):
            if target-e in count:
                return [count[target-e],i]
            count[e]=i
        