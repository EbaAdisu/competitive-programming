class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ns=""
        for e in s :
            if e.isalnum():
                ns+=e
        for i in range(len(ns)//2):
            if ns[i] != ns[-i-1]:
                return False
        return True