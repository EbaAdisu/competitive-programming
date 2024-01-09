class FrequencyTracker:

    def __init__(self):
        self.nums = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        prev = self.nums[number]
        if self.freq[prev]<=1:
            self.freq.pop(prev)
        else:
            self.freq[prev]-=1
        self.nums[number]+=1
        self.freq[prev+1]+=1

    def deleteOne(self, number: int) -> None:
        prev= self.nums[number]
        if prev <=1:
            self.nums.pop(number )
        else:
            self.nums[number]-=1
        if self.freq[prev]<=1:
            self.freq.pop(prev)
        else:
            self.freq[prev]-=1
        self.freq[prev-1]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)