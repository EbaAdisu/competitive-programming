class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        incre = True
        if len(arr) < 3 or arr[0] > arr[1] or arr[-1] > arr[-2]:
            return False

        for i in range(len(arr) - 1):
            if incre and arr[i] > arr[i+1]:
                incre = False
            elif not incre and arr[i] < arr[i+1]:
                return False

            if arr[i] == arr[i+1]:
                return False
        
        return True