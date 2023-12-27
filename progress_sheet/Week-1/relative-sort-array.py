class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {arr2[i]:i for i in range(len(arr2))}
        arr = []
        ext = []
        for e in arr1:
            if e in pos:
                arr.append(e)
            else:
                ext.append(e)
        arr.sort(key = lambda x: pos[x])
        return arr + sorted(ext)
        