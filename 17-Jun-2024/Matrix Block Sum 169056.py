# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        presum = mat[:]
        m = len(mat)
        n = len(mat[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if i==0:
                    if j >0:
                        presum[i][j]+=presum[i][j-1]
                else:
                    if j==0:
                        presum[i][j]+=presum[i-1][j]
                    else:
                        presum[i][j]+=presum [i][j-1]+presum[i-1][j]-presum[i-1][j-1]
            ans+=[[0]*n]
        #print(presum )
        for i in range(m):
            for j in range(n):
                maxi=i+k if i+k+1<m else m-1
                maxj=j+k if j+k+1<n else n-1
                mini=i-k-1 if i-k>0 else -1
                minj=j-k-1 if j-k>0 else -1
                #print((mini,minj),(maxi,maxj))
                ans[i][j]=presum[maxi][maxj]
                if mini>=0 and minj>=0:
                    ans[i][j]+=presum[mini][minj]
                    #print((mini,minj),presum[mini][minj],end=" ")
                if minj>=0:
                    ans[i][j]-=presum[maxi][minj]
                    #print((maxi,minj),presum[maxi][minj],end =" ")
                if mini>=0:
                    ans[i][j]-=presum[mini][maxj]
                    #print((mini,maxj),presum[mini][maxj],end=" ")
                #print(ans[i][j],)
        return ans 