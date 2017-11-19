# [Ebay]
'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
'''

from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # Always key the larger heap has same size with smaller, or bigger than one in size.
        small, larger = self.heaps
        m = len(small) #maximum heap
        n = len(larger) #minimum heap
        if m == 0 and n == 0:
            heappush(larger, num)
            return
        if m == n:
            minInLarger = larger[0]
            if num >= minInLarger:
                heappush(larger, num)
            else:
                heappush(small, -num)
                maxInSmall = -heappop(small)
                heappush(larger, maxInSmall)
        else:
            # n == m+1
            #minInLarger = heappop(larger)
            #maxInSmall = -heappop(small)
            if num >= larger[0]:
                minInLarger = heappushpop(larger, num)
                heappush(small, -minInLarger)
            else:
                heappush(small, -num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        small, larger = self.heaps
        m = len(small)
        n = len(larger)
        if m == n:
            return (-small[0]+larger[0])*1.0/2
        else:
            return larger[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()