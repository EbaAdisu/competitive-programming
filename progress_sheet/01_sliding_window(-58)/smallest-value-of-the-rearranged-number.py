class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        elif num < 0:
            num = str(num)[1:]
            sNum = sorted(num,reverse= True)
            return int(''.join(sNum)) * -1
        else:
            num = str(num)
            sNum = sorted(num)
            t = 0
            while sNum[t] == '0':
                t += 1
            sNum[t], sNum[0] = sNum[0], sNum[t] 

            return int(''.join(sNum))

        