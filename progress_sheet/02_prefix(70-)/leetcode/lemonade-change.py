class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i, e in enumerate(bills):
            if e == 5:
                five += 1
            elif e == 10:
                if not five: return False
                ten += 1
                five -= 1
            elif e == 20:
                t = 3
                if ten:
                    ten -= 1
                    t -= 2
                if five < t: return False
                five -= t
        return True
                