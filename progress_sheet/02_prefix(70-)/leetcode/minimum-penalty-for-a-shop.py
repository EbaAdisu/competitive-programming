class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y = 0
        for i in range(len(customers)-1, -1, -1):
            if customers[i] == 'Y':
                y += 1
        n = 0
        ind = 0
        mini = y
        for i, e in enumerate(customers):
            penal = n + y
            if penal < mini:
                mini = penal
                ind = i
            if e == 'N':
                n += 1
            else:
                y -= 1
        penal = n
        if penal < mini:
            ind = i + 1

        return ind





        