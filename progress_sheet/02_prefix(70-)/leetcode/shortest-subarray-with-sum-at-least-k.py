class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        positions = {0:-1}
        monotonic_que = deque([0])
        presum = 0
        answer = len(nums) + 5
        for r, e in enumerate(nums):
            presum += e
            while monotonic_que and monotonic_que[-1] > presum:
                left = monotonic_que.pop()
            monotonic_que.append(presum)
            positions[presum] = r
            while monotonic_que and monotonic_que[0] <= presum - k:
                left = monotonic_que.popleft()
                answer = min(answer, r - positions[left])
        return answer if answer != len(nums) + 5 else -1