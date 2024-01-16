class RandomizedSet:

    def __init__(self):
        self.count = Counter()
        self.li = []

    def insert(self, val: int) -> bool:
        if val in self.count:
            return False
        ind = len(self.li)
        self.li += [val]
        self.count[val] = ind

        return True

        

    def remove(self, val: int) -> bool:
        if val not in self.count:
            return False
        ind = self.count[val]
        sec = len(self.li) - 1
        self.count[self.li[sec]] = ind

        self.li[sec],self.li[ind] = self.li[ind],self.li[sec] 

        self.li.pop()
        self.count.pop(val)

        return True
        

    def getRandom(self) -> int:
        ind = random.randint(0,len(self.li)-1)
        return self.li[ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()