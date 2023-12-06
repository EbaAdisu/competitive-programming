class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans_str=[]
        ans_len=float('inf')
        for i,w in enumerate(list1):
            if w in list2:
                j=list2.index(w)
                if j+i<ans_len:
                    ans_str=[w]
                    ans_len=i+j
                elif j+i==ans_len:
                    ans_str+=[w]
        return ans_str