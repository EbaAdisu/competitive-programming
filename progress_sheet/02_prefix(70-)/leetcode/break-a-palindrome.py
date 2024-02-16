class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        pali = list(palindrome)
        for i, e in enumerate(pali):
            if len(pali)%2 and i == len(pali)//2:
                continue
            if e != 'a':
                pali[i] = 'a'
                return ''.join(pali)
        if len(pali) > 1:
            pali[-1] = 'b'
            return ''.join(pali)
        return ''

        