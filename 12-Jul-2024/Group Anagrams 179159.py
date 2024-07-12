# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import*
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        return anagrams.values()
        