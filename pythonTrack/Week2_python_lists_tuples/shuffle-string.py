class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_list=list(s)
        for index in range(len(s)):
            shuffled_list[indices[index]]=s[index]
        shuffled_str=''
        for char in shuffled_list:
            shuffled_str+=char
        return shuffled_str