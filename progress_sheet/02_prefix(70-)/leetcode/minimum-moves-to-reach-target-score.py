class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        double = maxDoubles
        while target > 1:
            if not double:
                return ans + target -1
            if double and target%2 == 0:
                double -= 1
                target //= 2 
                ans += 1
            else:
                ans += 1
                target -= 1
        return ans
        