class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd=[str(i) for i in range(1,10,2)]
        for i in range(len(num)-1,-1,-1):
            if num[i] in odd:
                return num[:i+1]
        return ""