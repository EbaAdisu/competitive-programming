class OrderedStream:

    def __init__(self, n: int):
        self.dic={i:[] for i in range(n)}
        self.i=0
        self.n=n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dic[idKey-1]=[value]
        ans=[]
        while self.i<self.n:
            if self.dic[self.i]==[]:
                break 
            ans+=self.dic[self.i]
            self.i+=1
        #print(self.dic,self.i )
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)