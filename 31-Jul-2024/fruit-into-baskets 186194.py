# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        window = Counter()
        answer = l = 0
        for ind in range(N):
            fruit = fruits[ind]
            window[fruit] += 1
            while len(window) > 2:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1
            answer = max(answer, ind - l + 1)
        return answer

        