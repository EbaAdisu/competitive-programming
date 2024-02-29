class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        col = {2:'a b c',3:'d e f',4:'g h i',5:'j k l',6:'m n o',7:'p q r s',8:' t u v',9:' w x y z'}
        ans = []
        n = len(digits)
        if n == 0:
            return []
        elif n == 1:
            return col[int(digits)].split()
        elif n == 2:
            fir = col[int(digits[:1])].split()
            sec = col[int(digits[1:2])].split()
            for f in  fir:
                for s in sec:
                    st = f + s
                    ans += [st]
        elif n == 3:
            fir = col[int(digits[:1])].split()
            sec = col[int(digits[1:2])].split()
            thi = col[int(digits[2:3])].split()
            for f in  fir:
                for s in sec:
                    for t in thi:
                        st = f + s + t
                        ans += [st]
        elif n == 4:
            fir = col[int(digits[:1])].split()
            sec = col[int(digits[1:2])].split()
            thi = col[int(digits[2:3])].split()
            fou = col[int(digits[3:4])].split()
            for f in  fir:
                for s in sec:
                    for t in thi:
                        for fr in fou:
                            st  = f+s+t+fr
                            ans += [st]
        return ans


