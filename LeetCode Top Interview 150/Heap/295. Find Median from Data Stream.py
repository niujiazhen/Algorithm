class MedianFinder:
    def __init__(self):
        self.lowerHalf = []  # max-heap (store negatives)
        self.upperHalf = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowerHalf, -num)

        # Balance largest of lowerHalf into upperHalf
        heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))

        # Maintain size property
        if len(self.upperHalf) > len(self.lowerHalf):
            heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))

    def findMedian(self) -> float:
        if len(self.lowerHalf) > len(self.upperHalf):
            return -self.lowerHalf[0]
        return (-self.lowerHalf[0] + self.upperHalf[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == '__main__':
    m=MedianFinder()
