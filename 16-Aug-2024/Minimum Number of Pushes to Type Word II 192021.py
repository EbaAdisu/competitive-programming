# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = sorted(Counter(word).values(), reverse = True)
        return sum(counter[:8])*1 + sum(counter[8:16]) * 2 + sum(counter[16:24])*3 + sum(counter[24:])*4


        