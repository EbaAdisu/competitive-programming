class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        les=[]
        piv=[]
        upper=[]
        for e in nums:
            if e>pivot:
                upper+=[e]
            elif e<pivot:
                les+=[e]
            else:
                piv+=[e]
        return les+piv+upper 