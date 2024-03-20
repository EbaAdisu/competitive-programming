class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        nums = [(nums[i],i) for i in range(len(nums))]
        def merge(l,r):
            if l == r:
                return[nums[l]]
            mid = (l+r)//2
            left = merge(l, mid)
            right = merge(mid + 1,r)
            return mergeSort(left, right)
        def mergeSort(left, right):
            f = 0 
            s = 0
            pre = 0
            ans = []
            while f < len(left) and s < len(right):
                if left[f][0] <= right[s][0]:
                    count[left[f][1]] += pre
                    ans.append(left[f])
                    f += 1
                else:
                    pre += 1
                    ans.append(right[s])
                    s += 1
            while f < len(left):
                ans.append(left[f])
                count[left[f][1]] += pre
                f += 1
            ans.extend(right[s:])
            return ans
        merge(0,len(nums) - 1)
        return count
        