# Problem: Corporate Flight Bookings - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0]*(n+1)
        for l,r,v in bookings:
            prefix_sum[l-1] += v
            prefix_sum[r] -= v
        for ind in range(1,n+1):
            prefix_sum[ind] += prefix_sum[ind-1]
        return prefix_sum[:-1]