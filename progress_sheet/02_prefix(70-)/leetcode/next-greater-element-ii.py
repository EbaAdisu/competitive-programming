class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        double = nums*2
        nextNum = defaultdict(lambda: -1)
        stack = []
        for i,e in enumerate(double):
            while stack and stack[-1][0] < e:
                nextNum[(stack.pop()[1])%len(nums)] = e
            stack += [(e,i)]
        for i in range(len(nums)):
            nums[i] = nextNum[i]
        return nums