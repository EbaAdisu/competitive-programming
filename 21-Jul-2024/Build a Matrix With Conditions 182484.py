# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def indify(arr):
            indicies = {}
            for ind in range(len(arr)):
                indicies[arr[ind]] = ind
            return indicies
        def topo(cond):
            graph = defaultdict(list)
            degree = Counter()
            for pre, post in cond:
                graph[pre].append(post)
                degree[post] += 1
            fringe = [i for i in range(1,k+1) if degree[i] ==0]
            ret = []
            while fringe:
                ret.extend(fringe)
                new_fringe = [] 
                for ind in fringe:
                    for new_ind in graph[ind]:
                        degree[new_ind] -= 1
                        if degree[new_ind] == 0:
                            new_fringe.append(new_ind)
                fringe = new_fringe
            return ret
        rows = topo(rowConditions)
        cols = topo(colConditions)
        if len(rows) < k or len(cols) < k:
            return []
        row_ind = indify(rows)
        col_ind = indify(cols)
        mat = [[0]*k for _ in range(k)]
        for val in rows:
            mat[row_ind[val]][col_ind[val]] = val
        return mat