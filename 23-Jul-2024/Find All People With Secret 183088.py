# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def sortKey(x):
            return x[2]
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            y = find(y)
            x = find(x)
            if x == y:
                return -1
            if size[x] >= size[y]:
                parent[y] = parent[x]
            else:
                parent[x] = parent[y]
        parent = {p:p for p in range(n)}
        size = {p:0 for p in range(n)}
        meets = defaultdict(set)
        for l,r,m in meetings:
            meets[m].add((l,r))
        union(0,firstPerson)
        ans = set([0, firstPerson])
        for time in sorted(meets):
            ini = find(0)
            for p1, p2 in meets[time]:
                union(p1, p2)
            for p1, p2 in meets[time]:
                ini = find(0)
                if find(p1) == ini:
                    ans.add(p1)
                    ans.add(p2)
                    # print(p1,find(p1))
                else:
                    parent[p1] = p1
                    parent[p2] = p2
            # print(time, meets[time], ini,ans)

        # print(parent)
        return ans