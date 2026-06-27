class MedianFinder:

    def __init__(self):
        self.a = [] #small
        self.b = [] # buf
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.a,-num)

        heapq.heappush(self.b,-heapq.heappop(self.a))

        if len(self.a) < len(self.b):
            heapq.heappush(self.a,-heapq.heappop(self.b))



        

    def findMedian(self) -> float:
        if len(self.a) > len(self.b):
            return -self.a[0]
        return (-self.a[0] + self.b[0])/2
        
        