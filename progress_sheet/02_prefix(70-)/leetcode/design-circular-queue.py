class MyCircularQueue:

    def __init__(self, k: int):
        self.que = deque()
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if len(self.que) < self.size:
            self.que.append(value)
            return True
        return False 
        

    def deQueue(self) -> bool:
        if self.que:
            self.que.popleft()
            return True
        return False
        

    def Front(self) -> int:
        if self.que:
            return self.que[0]
        return -1
        

    def Rear(self) -> int:
        if self.que:
            return self.que[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.que) == 0
        

    def isFull(self) -> bool:
        return len(self.que) == self.size

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()