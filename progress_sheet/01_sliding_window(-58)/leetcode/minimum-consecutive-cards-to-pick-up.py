class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        ans = n + 1
        pos = defaultdict(int)

        for r, e in enumerate(cards):
            if e in pos:
                ans = min(ans, r - pos[e] + 1)
            pos[e] = r

        return -1 if ans == n + 1 else ans