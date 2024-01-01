class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        pre = 0
        for i, e in enumerate(costs):
            pre += e
            if pre > coins:
                return i
        return i + 1