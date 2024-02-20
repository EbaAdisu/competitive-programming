class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        que = deque(senate)
        R = D = 0
        while count['R'] and count['D']:
            left = que.popleft()
            if left == 'R':
                if not R:
                    D += 1
                    que.append(left)
                else:
                    R -= 1
                    count['R'] -= 1
            if left == 'D':
                if not D:
                    R += 1
                    que.append(left)
                else:
                    D -= 1
                    count['D'] -= 1
            # print(que,count)
        if que[0] == 'R': return 'Radiant'
        return 'Dire'
        