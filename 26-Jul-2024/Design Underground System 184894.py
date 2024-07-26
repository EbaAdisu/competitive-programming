# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.cust = {}
        self.station = defaultdict(dict)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cust[id] = (stationName, t)
        # print("checkin", id, stationName)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        pre_s, pre_t = self.cust[id] 
        if pre_s in self.station[stationName]:
            self.station[stationName][pre_s][0] += 1
            self.station[stationName][pre_s][1] += (t - pre_t)
        else:
            self.station[stationName][pre_s] = [1, t - pre_t]

        # print("checkout", id, stationName, pre_s,self.station[stationName][pre_s])

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print("getAverage",endStation,startStation,self.station[endStation][startStation])
        return self.station[endStation][startStation][1]/self.station[endStation][startStation][0]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)