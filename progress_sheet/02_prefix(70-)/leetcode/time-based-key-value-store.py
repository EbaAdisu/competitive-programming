class TimeMap:

    def __init__(self):
        self.ds = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        times = self.ds[key]
        if not times or times[0][0] > timestamp:
            return ''
        l = 0
        r = len(times) - 1
        while l < r:
            mid = (l+r+1)//2
            if times[mid][0] <= timestamp:
                l = mid
            else:
                r = mid - 1
        return times[l][1]
    