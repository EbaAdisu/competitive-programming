class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse = True)
        n = len(tasks)
        t = 0

        for i in range(3, n,4):
            processorTime[t] += tasks[i]
            t += 1
        return max(processorTime)

        

        