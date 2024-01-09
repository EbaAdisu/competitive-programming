class Bitset:

    def __init__(self, size: int):
        self.bits = {i:0 for i in range(size)}
        self.ones = 0
        self.rev = False 

    def fix(self, idx: int) -> None:
        if not self.rev:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones += 1
        else:
            if self.bits[idx] == 1:
                self.bits[idx] = 0 
                self.ones += 1
                
    def unfix(self, idx: int) -> None:
        if not self.rev:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones -= 1
        else:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones -= 1

    def flip(self) -> None:
        self.rev = not self.rev
        self.ones = len(self.bits) - self.ones 

    def all(self) -> bool:
        return self.ones == len(self.bits)

    def one(self) -> bool:
        return self.ones > 0
        

    def count(self) -> int:
        return self.ones
        

    def toString(self) -> str:
        if self.rev:
            bits=[str((i+1)%2) for i in self.bits.values()]
        else:
            bits=[str(i) for i in self.bits.values()]
        return "".join(bits)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()