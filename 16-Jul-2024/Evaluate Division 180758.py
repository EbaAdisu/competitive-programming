# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(values)):
            a, b = equations[i]
            v = values[i]
            graph[a].append((b, v))
            graph[b].append((a, 1/v))
            
        def dfs(start, total):
            visited.add((start))
            if start == target:
                return total
            for new_start, val in graph[start]:
                if new_start not in visited:
                    ret = dfs(new_start, total * val)
                    if ret != -1:
                        return ret
            return -1

        ans = []
        for start, target in queries:
            visited = set()
            if start in graph:
                ans.append(dfs(start,1))
            else:
                ans.append(-1)
        return ans