# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)
        while len(heap) > 1:
            y = - heappop(heap)
            x = - heappop(heap)
            if y > x:
                heappush(heap, x - y)
            print(y,x,heap)
        return -sum(heap)
            
        