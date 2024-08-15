# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = twenty = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five:
                    five -= 1
                else:
                    return False
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


        