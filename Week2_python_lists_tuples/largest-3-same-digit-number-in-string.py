class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2] and num[i]>ans:
                ans=num[i]
        return ans*3