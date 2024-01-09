class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            maxi = 0
            for j in range(len(arr) - i):
                if arr[j] > arr[maxi]:
                    maxi = j
            arr[:maxi+1] = arr[:maxi+1][::-1]
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
            ans +=[maxi+1,len(arr)-i ]
        return ans