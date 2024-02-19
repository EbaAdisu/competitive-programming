class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def neg():return -1
        stack = []
        nextElement = defaultdict(neg)
        for e in nums2:
            while stack and stack[-1] < e:
                nextElement[stack.pop()] = e
            stack += [e]
            print(stack)
        return [nextElement[num] for num in nums1]
        
        
        