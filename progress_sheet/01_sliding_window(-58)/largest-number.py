class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nnum=list(map(str,nums))
        for i in range(len(nnum)):
            for j in range(i + 1, len(nnum)):
                if nnum[j] + nnum[i] > nnum[i] + nnum[j]:
                    nnum[i], nnum[j] = nnum[j], nnum[i]
        return str(int("".join(nnum)))
        