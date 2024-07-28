# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = Counter()
        temp = Counter()
        max_left = 0
        l = 0
        ans = 0
        for r, e in enumerate(nums):
            counter[e] += 1
            temp[e] += 1
            while len(counter) > k:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0: counter.pop(nums[l])
                l += 1
            while max_left < l:
                temp[nums[max_left]] -= 1
                if temp[nums[max_left]] == 0: temp.pop(nums[max_left])
                max_left += 1
            while len(temp) == k:
                temp[nums[max_left]] -= 1
                if temp[nums[max_left]] == 0: temp.pop(nums[max_left])
                max_left += 1
            if len(counter) == k:
                ans += max_left - l
        return ans
                
            