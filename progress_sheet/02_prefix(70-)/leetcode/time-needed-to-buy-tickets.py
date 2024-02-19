class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        dif = 0
        val = tickets[k]
        for i in range(n):
            if i < k and tickets[i] < val:
                dif += val - tickets[i]
            if i > k and tickets[i] < val-1:
                dif += val - tickets[i]-1
        return (val-1) * (n) + k+1 - dif
        