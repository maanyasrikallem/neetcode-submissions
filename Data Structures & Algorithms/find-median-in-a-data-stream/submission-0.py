import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []   # smaller half (store negatives)
        self.minHeap = []   # larger half

    def addNum(self, num: int) -> None:

        # Decide which heap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # Rebalance

        # maxHeap can have at most 1 extra element
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # minHeap should never have more elements
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:

        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        return (-self.maxHeap[0] + self.minHeap[0]) / 2