class Robot:

    def __init__(self, width: int, height: int):
        self.m = (width) * 2 + (height - 2) * 2
        self.p = 0
        self.bu = True
        self.dire = ['East','North', 'West','South']

        self.pos = [
            {i:[i,0] for i in range(1,width)}, 
            {i:[width - 1, i - width + 1] for i in range(width, width + height - 1)}, 
            {i:[width*2+height-3 - i, height -1 ] for i in range(width*2+height-3,width+height-2,-1 )}, 
            {i:[0,self.m - i] for i in range(self.m-1,width*2+height-3,-1 )}
        ]

        self.pos[-1][0] = [0,0]

        # print(self.pos,self.m)

    def step(self, num: int) -> None:

        self.bu = False
        self.p += num 
        self.p %= self.m

    def getPos(self) -> List[int]:

        for k in self.pos:
            if self.p in k:
                return k[self.p]

    def getDir(self) -> str:

        if self.bu and self.p == 0:
            return 'East'
        
        for i in range(4):
            if self.p in self.pos[i]:
                return self.dire[i]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()