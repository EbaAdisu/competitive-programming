class ATM:

    def __init__(self):
        self.bill=[20,50,100,200,500]
        self.count={i:0 for i in self.bill}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.count[self.bill[i]]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        widow=[0]*5
        for i in range(4,-1,-1):
            bill = self.bill[i]
            count =self.count[bill]
            mini= min(amount//bill,count)
            if mini > 0:
                widow[i]=mini
                amount-=mini*bill
        if amount:
            return [-1]
        for i in range(4,-1,-1):
            self.count[self.bill[i]]-=widow[i]
        return widow 


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)