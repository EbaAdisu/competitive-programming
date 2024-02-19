class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stack += [val]
        if not self.min or self.min[-1] >= val:
            self.min += [val]

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min[-1] == val:
            self.min.pop()
        return val
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()