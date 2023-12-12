class UndergroundSystem:

    def __init__(self):
        self.register = {}
        self.average = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.register[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        cinStation, cinTime = self.register.pop(id)
        self.average[(cinStation,stationName)]+=[t-cinTime]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        timeList=self.average[(startStation, endStation)]
        return sum(timeList)/len(timeList)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)