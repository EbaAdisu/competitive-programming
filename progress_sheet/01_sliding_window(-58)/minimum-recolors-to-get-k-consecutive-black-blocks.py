class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        change = 0
        for i in range(k):
            if blocks[i] == 'W':
                change += 1
        ans = change
        for i in range(k,len(blocks)):
            if blocks[i] == 'W':
                change += 1
            if blocks[i-k] == 'W':
                change -= 1


            ans = min(ans,change)
        return ans