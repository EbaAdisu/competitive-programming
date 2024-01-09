class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []

        f = 0
        s = 0
        
        while f < len(firstList) and s < len(secondList):
            left = max(firstList[f][0], secondList[s][0])
            right = min(firstList[f][1], secondList[s][1])
            if left<=right:
                ans += [[left,right]]


            if firstList[f][1] > secondList[s][1]:
                s += 1
            elif firstList[f][1] < secondList[s][1]:

                f += 1
            else:
                f+=1
                s+=1

        return ans
    

        