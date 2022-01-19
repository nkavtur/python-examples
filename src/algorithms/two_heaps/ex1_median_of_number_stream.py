from heapq import *


class MedianOfStream:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        print(self.max_heap, self.min_heap)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, heappop(self.min_heap))

    def find_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return self.min_heap[0] / 2 + -self.max_heap[0] / 2

        return -self.max_heap[0]


medianOfStream = MedianOfStream()
medianOfStream.insert_num(3)
medianOfStream.insert_num(1)
# print(medianOfStream.find_median())

medianOfStream.insert_num(5)
# print(medianOfStream.find_median())

medianOfStream.insert_num(4)
medianOfStream.insert_num(7)
# print(medianOfStream.find_median())
