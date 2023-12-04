class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        l=min(start,destination)
        r=max(start,destination)
        su=sum(distance[l:r])
        return min(su,sum(distance)-su)
        