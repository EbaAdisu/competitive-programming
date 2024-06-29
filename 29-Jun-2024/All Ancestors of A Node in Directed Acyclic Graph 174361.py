# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = Counter()
        for a, b in edges:
            graph[a].append(b)
            degree[b] += 1
        que = [ind for ind in range(n) if degree[ind] == 0]
        output = [[] for ind in range(n)]
        while que:
            new_que = []
            for ind in que:
                output[ind] = sorted(set(output[ind]))
                for new_ind in graph[ind]:
                    degree[new_ind] -= 1
                    output[new_ind].extend(output[ind] + [ ind]) 
                    if degree[new_ind] == 0:
                        new_que.append(new_ind)
            que = new_que
        return output




        