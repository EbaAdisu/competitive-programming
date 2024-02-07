class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] *(n+1)
        for l, r, v in bookings:
            ans[l-1] += v
            ans[r] -= v
        for i in range(1,n):
            ans[i] += ans[i-1]
        return ans[:-1]
        