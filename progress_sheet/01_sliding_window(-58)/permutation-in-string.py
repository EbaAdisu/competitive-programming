class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = Counter(s1)
        count2 = Counter()
        l = 0
        k = len(s1)

        for i in range(k):
            count2[s2[i]] += 1
        for r in range(k,len(s2)):
            if count1 == count2:
                return True
            count2[s2[r]] += 1
            count2[s2[r-k]] -= 1
            
        return count1 == count2

        