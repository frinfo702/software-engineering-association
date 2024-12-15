import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.Kth = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            # サイズをkに調整
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) < self.Kth:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
