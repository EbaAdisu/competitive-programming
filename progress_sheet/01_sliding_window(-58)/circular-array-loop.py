class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        bad = set()
        n = len(nums)
        for i,e in enumerate(nums):
            seen = set()
            if e in bad:
                continue
            curr = i
            pos = True if e >= 0 else False 
            pre = None
            while curr not in seen and curr not in bad:
                seen.add(curr)
                bad.add(curr)
                pre = curr
                curr = (e+curr)%n
                e = nums[curr]
                if pos and e<0 or not pos and e >=0:
                    pre = None
                    break
            if pre != None and pre != curr and len(seen) > 1:
                return True
        return False

        