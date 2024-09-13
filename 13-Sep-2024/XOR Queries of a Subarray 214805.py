# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        x = 0
        for e in arr:
            x ^= e
            xor.append(x)
        ans = []
        for l, r in queries:
            ans.append(xor[r+1]^xor[l])
        return ans


        