class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monotonic_stack = [] # increasing monotonic stack
        min_stack = []
        minimum_sofar = nums[0]
        for e in nums:
            minimum_sofar = min(e,minimum_sofar)
            min_stack.append(minimum_sofar)
        print(min_stack)
        for r in range(len(nums)-1,-1,-1):
            e = nums[r]
            while monotonic_stack and monotonic_stack[-1] < e:
                if monotonic_stack.pop() > min_stack[r]: return True
            monotonic_stack.append(e)
        return False