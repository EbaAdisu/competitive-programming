class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for k in count:
            amount = ceil(count[k] / (k+1))
            ans += (k+1)*amount
        return ans


        