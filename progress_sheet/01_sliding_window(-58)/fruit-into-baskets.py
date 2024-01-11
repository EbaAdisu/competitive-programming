class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        ans = 0
        for r, e in enumerate(fruits):
            basket[e] += 1
            while len(basket)>2:
                n = fruits[l]
                basket[n] -= 1
                if basket[n] == 0:
                    basket.pop(n)
                l+=1
            ans = max(ans,r-l+1)
        return ans