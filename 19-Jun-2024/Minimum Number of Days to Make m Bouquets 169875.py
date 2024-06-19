# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def kadj(bloomDay, k):
            N = len(bloomDay)
            max_que = deque()
            for ind in range(k):
                while max_que and max_que[-1] < bloomDay[ind]:
                    max_que.pop()
                max_que.append(bloomDay[ind])
            blooms = [max_que[0]]
            for ind in range(N-k):
                if max_que[0] == bloomDay[ind]:
                    max_que.popleft()
                while max_que and max_que[-1] < bloomDay[ind + k]:
                    max_que.pop()
                max_que.append(bloomDay[ind + k])
                blooms.append(max_que[0])
            return blooms

        def valid(day, blooms):
            pre = -k
            total = 0
            for ind in range(len(blooms)):
                if blooms[ind] <= day and ind >= pre + k:
                    total += 1
                    pre = ind
            return total >= m
        
        def binary(bloom):
            l, r = min(bloom), max(bloom)
            if valid(l,bloom):
                return l
            elif not valid(r, bloom):
                return -1
            while l < r:
                mid = (l + r)//2
                if valid(mid, bloom):
                    r = mid
                else:
                    l = mid + 1
            return r

        blooms = kadj(bloomDay, k)
        # print(blooms)
        return binary(blooms)