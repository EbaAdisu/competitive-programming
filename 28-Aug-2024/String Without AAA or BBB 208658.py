# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ''
        while a and b:
            if s:
                if s[-1] == 'a':
                    if a > b:
                        l = 1
                    else:
                        l = min(2,b)
                    s += 'b' * l
                    b -= l
                else:
                    if a < b:
                        l = 1
                    else:
                        l = min(2,a)
                    s += 'a' * l
                    a -= l
            else:
                if a > b:
                    l = min(2,a)
                    s += 'a'*l
                    a -= l
                else:
                    l = min(2,b)
                    s += 'b'*l
                    b -= l
            # print(a,b,s)

        s += 'a'*a
        s += 'b'*b
        return s

        