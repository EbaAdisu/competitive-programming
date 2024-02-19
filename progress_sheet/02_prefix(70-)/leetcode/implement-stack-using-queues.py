class MyStack:

    def __init__(self):
        self.que = deque()
        self.ext = deque()
        

    def push(self, x: int) -> None:
        self.que.append(x)
        

    def pop(self) -> int:
        while len(self.que) > 1:
            self.ext.append(self.que.popleft())
        val = self.que.popleft()
        while self.ext:
            self.que.append(self.ext.popleft())
        return val
        

    def top(self) -> int:
        while self.que:
            val = self.que.popleft()
            self.ext.append(val)
        while self.ext:
            self.que.append(self.ext.popleft())
        return val
        

    def empty(self) -> bool:
        return len(self.que) == 0 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()