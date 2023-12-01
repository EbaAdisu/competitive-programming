class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"M":1000, "D":500, "C":100, "L":50, "X":10,"V":5, "I":1}
        sum=0
        ro=s.upper()
        for i in range(len(ro)):
            if i<len(ro)-1:
                if dic[ro[i]]<dic[ro[i+1]]:
                    sum-=dic[ro[i]]
                else:
                    sum+=dic[ro[i]]
            else:
                sum+=dic[ro[i]]	
        return sum		
        