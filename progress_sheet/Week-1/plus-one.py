class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        t = 0
        for i in range(len(digits) - 1, -1, -1 ):
            digits[i] += t
            t = 0
            if digits[i] == 10:
                t = 1
                digits[i] = 0
            else:
                return digits
        if t:
            digits = [1] + digits
        
        return digits