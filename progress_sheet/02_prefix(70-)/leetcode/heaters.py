class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def validate(r):
            h = 0
            for i in range(len(heaters)):
                while h < len(houses) and heaters[i] - r <= houses[h] <= heaters[i] + r:
                    h += 1
                # print(h,i)
            return h == len(houses)

        l = 0
        r = max(heaters[-1], houses[-1]) - min(heaters[0], houses[0])
        while l < r:
            mid = (l + r)//2
            if validate(mid):
                r = mid
            else:
                l = mid + 1
            # print((l,r),mid)
        return r

        