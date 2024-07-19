# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        N = len(nums1)
        nums = [nums1[i] - nums2[i] for i in range(N)]
        def merge(l,r):
            if l == r:
                return [nums[l]]
            mid = (l+r)//2
            left = merge(l,mid)
            right = merge(mid+1,r)
            return merge_sort(left, right)
        def merge_sort(left,right):
            nonlocal total
            for num in right:
                total += bisect_right(left, num + diff)
                # print(num, bisect_right(left,num+diff))
            ans = []
            f, s = 0,0
            while f < len(left) and s < len(right):
                if left[f] > right[s]:
                    ans.append(right[s])
                    s += 1
                else:
                    ans.append(left[f])
                    f += 1
            ans.extend(left[f:])
            ans.extend(right[s:])
            return ans
        total = 0
        
        merge(0,N-1)



        return total
        