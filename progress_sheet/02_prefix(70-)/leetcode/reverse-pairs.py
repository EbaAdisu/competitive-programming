class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pairs = [0]
        def merge(l,r):
            if l == r:
                return[nums[l]]
            mid = (l+r)//2
            left = merge(l, mid)
            right = merge(mid + 1,r)
            return mergeSort(left, right)
        def mergeSort(left, right):
            for e in left:
                pairs[0] += bisect_left(right,e/2) 
            f = 0 
            s = 0
            ans = []

            while f < len(left) and s < len(right):
                if left[f] <= right[s]:
                    ans.append(left[f])
                    f += 1
                else:
                    ans.append(right[s])
                    s += 1
            ans.extend(left[f:])
            ans.extend(right[s:])
            return ans
        merge(0, len(nums) - 1)
        print(pairs)
        return pairs[0]