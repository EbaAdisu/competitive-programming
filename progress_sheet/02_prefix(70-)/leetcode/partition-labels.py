class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ind = {s[i]:i for i in range(len(s))}
        ans = []
        part = curr = 0
        for i, e in enumerate(s):
            part += 1
            curr = max(curr,ind[e])
            if i == curr:
                ans += [part]
                part, curr = 0, i + 1
        return ans