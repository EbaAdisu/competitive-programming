class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            if nums[i] < 0:
                dire = -1
            else:
                dire = 1

            t = 0
            pos = i

            while t <= len(nums):
                if nums[pos] * dire < 0 or nums[pos] == 0 and dire == -1:
                    break

                pos += nums[pos]
                pos %= len(nums)
                if t == 0 and pos ==i:
                    break
                elif pos == i:
                    return True

                t += 1

        return False