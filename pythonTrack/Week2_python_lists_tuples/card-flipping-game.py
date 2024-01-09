class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        count=set(fronts+backs)
        for i in range(len(backs )):
            if backs[i] ==fronts[i]:
                count.discard(backs[i])
        return min(count) if count else 0