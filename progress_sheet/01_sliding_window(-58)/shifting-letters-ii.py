class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        shift = [0]*(len(s)+1)
        for l, r, v in shifts:
            v = 1 if v == 1 else -1
            shift[l] += v
            shift[r+1] -= v
        for i in range(1,len(shift)):
            shift[i]+=shift[i-1]
        print(shift)
        ans = ''
        for i in range(len(shift)-1):
            ans += letters[(letters.index(s[i])+shift[i])%26]
            print(letters.index(s[i]))
        return ans