# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[1][0] in edges[0]:
            return edges[1][0]
        return edges[1][1]