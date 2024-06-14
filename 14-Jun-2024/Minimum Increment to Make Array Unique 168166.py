# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        ans = 0
        pre = nums[0]
        for ind in range(N):
            if pre > nums[ind]:
                ans += pre-nums[ind]
            pre = pre + 1
            if nums[ind] + 1 > pre:
                pre = nums[ind] + 1          
        return ans
    
        ## gready
        




        ## heap aproach
        nums = sorted(counter)
        heap = nums[:]
        heapify(heap)
        pre = heappop(heap)
        counter[pre] -= 1
        ans= 0
        if counter[pre] > 0:
            ans += counter[pre]
            if pre + 1 not in counter:
                heappush(heap, pre+1)
            counter[pre+1] += counter[pre]
        while heap:
            next_min = heappop(heap)
            counter[next_min] -= 1
            if counter[next_min] > 0:
                ans += counter[next_min]
                if next_min + 1 not in counter:
                    heappush(heap, next_min+1)
                counter[next_min+1] += counter[next_min]
        return ans
        