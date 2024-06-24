# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for ind in range(m-1,-1,-1):
            nums1[ind], nums1[ind + n] = nums1[ind + n],nums1[ind]
        # print(nums1)

        place = 0
        f = n
        s = 0
        while f<(m+n) and s < n:
            if nums1[f] >= nums2[s]:
                nums1[(place)%(m+n) ] = nums2[s]
                s += 1
            else:
                nums1[(place)%(m+n) ] = nums1[f]
                f += 1
            place += 1
        while f<(m+n):
            nums1[(place)%(m+n) ] = nums1[f]
            f += 1
            place += 1
        while s < n:
            nums1[(place)%(m+n) ] = nums2[s]
            s += 1
            place += 1


            
        