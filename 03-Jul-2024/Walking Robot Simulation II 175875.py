# Problem: Walking Robot Simulation II - https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.mod = (width + height)*2 - 4
        self.curr = 0
        self.first = True
        

    def step(self, num: int) -> None:
        self.curr += num 
        self.curr%= self.mod
        self.first = False
        

    def getPos(self) -> List[int]:
        x = 0
        y = 0
        if self.curr == 0:
            return [0,0]
        if self.curr < self.w:
            x = self.curr
            y = 0
        elif self.curr < self.w + self.h - 1:
            x = self.w-1
            pos = self.curr - (self.w -1)
            y = pos%self.h
            # print(self.curr, x,y)

        elif self.curr < self.w * 2 + self.h - 3:
            pos = self.curr - (self.w + self.h-3)
            x = -pos%self.w
            y = self.h-1
        else:
            x = 0
            pos = self.curr - (self.w * 2 + self.h - 4)
            y = -pos%self.h
        return [x,y]

    def getDir(self) -> str:
        if self.curr  == 0:
            if self.first:
                return 'East'
            return 'South'
        elif self.curr < self.w:
            return 'East'
        elif self.curr < self.w + self.h - 1:
            return 'North'
        elif self.curr < self.w*2 + self.h -2:
            return 'West'
        return 'South'
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()