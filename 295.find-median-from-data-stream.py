#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:
    
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        if self.count % 2 == 0:
            heappush(self.minheap, -heappushpop(self.maxheap, -num))
        else:
            heappush(self.maxheap, -heappushpop(self.minheap, num))

    def findMedian(self) -> float:
        if self.count % 2 != 0:
            return float(-self.maxheap[0])
        return float(-self.maxheap[0] + self.minheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

