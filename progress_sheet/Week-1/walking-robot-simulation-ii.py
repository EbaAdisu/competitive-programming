class Robot:

    def __init__(self, width: int, height: int):
        self.m = (width) * 2 + (height - 2) * 2
        self.w = width -1
        self.h = height -1
        self.p = 0
        self.bu = True
        

        self.dire = {'East':[i for i in range(1,width)], 'North': [i for i in range(width,width+height - 1)], 'West':[i for i in range(width*2+height-3,width+height-2,-1 )], 'South':[0]+[i for i in range(self.m-1,width*2+height-3,-1 )]}

        print(self.dire,self.m)
    def step(self, num: int) -> None:
        if num != 0:
            self.bu = False
        self.p += num 
        self.p %= self.m

    def getPos(self) -> List[int]:
        
        t = 0
        for k in self.dire:
            if self.p in self.dire[k]:
                if t == 0:
                    return [self.dire[k].index(self.p)+1,0]
                elif t == 1:
                    return [self.w,self.dire[k].index(self.p) + 1]
                elif t == 2:
                    return [self.dire[k].index(self.p),self.h]
                elif t == 3:
                    return [0,self.dire[k].index(self.p)]
            t += 1

    def getDir(self) -> str:
        if self.bu and self.p == 0:
            print(1)
            return 'East'
        

        for k in self.dire:
            if self.p in self.dire[k]:
                return k
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()