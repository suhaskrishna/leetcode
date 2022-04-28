class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.travel = collections.defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check_in.pop(id)
        
        self.travel[(startStation, stationName)][0] += t-startTime
        self.travel[(startStation, stationName)][1] += 1 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travel[(startStation, endStation)][0]/self.travel[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)