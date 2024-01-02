class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            su = numbers[l] + numbers[r]
            if su == target:
                return [l + 1,r + 1]
            elif su > target:
                r -= 1
            else:
                l += 1



