# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        t = k -1
        while len(arr) > 1:
            arr.pop(t)
            t = (t + k -1 ) % len(arr)
    
        return arr[0]