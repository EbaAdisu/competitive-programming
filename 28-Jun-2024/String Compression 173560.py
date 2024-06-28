# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        count = 0
        pre = ''
        for char in chars:
            if char != pre:
                if count > 1:
                    s += pre + str(count)
                else:
                    s += pre
                count = 1
            else:
                count += 1
            pre = char
        if count > 1:
            s += pre + str(count)
        else:
            s += pre
        for i in range(len(s)):
            chars[i] = s[i]
        # print(s,chars)
        return len(s)

        