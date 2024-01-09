class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        k=len(arr)/4
        if len(arr)==1:
            return arr[0 ]
        t=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                t+=1
            else:
                t=1
            if t>k:
                return arr[i ]
        