# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
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

        parent = {i:i for i in range(len(accounts))}
        size = {i:0 for i in range(len(accounts))}
        num = set([i for i in range(len(accounts))])
        for i in range(len(accounts)):
            for e in accounts[i][1:]:
                # union(e,i)
                if e in parent:
                    union(i, e)
                else:
                    parent[e] = find(i)
        ans = defaultdict(list)

        for k in parent:
            if k not in num:
                ans[find(k)].append(k)
        
        ret = []
        for i in ans:
            temp = [accounts[i][0]] + sorted(ans[i])
            ret.append(temp)
        return ret