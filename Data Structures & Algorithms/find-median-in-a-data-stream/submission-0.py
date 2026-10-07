class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.large) and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.large) - len(self.small) > 1:
            heapq.heappush(self.small,-(heapq.heappop(self.large)))
        elif len(self.large) - len(self.small) < -1:
            heapq.heappush(self.large,-(heapq.heappop(self.small)))


    def findMedian(self) -> float:
        if len(self.large) - len(self.small) > 0:
            return self.large[0]
        elif len(self.large) - len(self.small) < 0:
            return -self.small[0]
        else:
            return (float(self.large[0]) + float(-self.small[0]))/2.0

        