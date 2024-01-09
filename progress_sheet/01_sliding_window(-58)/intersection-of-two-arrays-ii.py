class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        f = 0
        s = 0
        ans = []
        while f < len(nums1) and s < len(nums2):
            if nums1[f] == nums2[s]:
                ans += [nums1[f]]
                f += 1
                s += 1
            elif nums1[f] > nums2[s]:
                s += 1
            elif nums1[f] < nums2[s]:
                f += 1
        return ans
        