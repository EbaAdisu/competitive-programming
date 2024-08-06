# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = Counter()
        for a,b in edges:
            degree[a] += 1
            degree[b] += 1
            graph[a].append(b)
            graph[b].append(a)
        ans = []
        fringe = [i for i in range(n) if degree[i] <= 1]
        while fringe:
            new_fringe = []
            ans = fringe
            for ind in fringe:
                for new_ind in graph[ind]:
                    degree[new_ind] -= 1
                    if degree[new_ind] == 1:
                        new_fringe.append(new_ind)

            fringe = new_fringe
        return ans
            