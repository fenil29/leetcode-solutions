class MedianFinder:

    def __init__(self):
        self.numList = []

    def addNum(self, num: int) -> None:
        if len(self.numList) == 0:
            self.numList.append(num)
        else:
            start = 0
            end = len(self.numList)-1
            while start <= end:
                mid = math.floor((start+end)/2)
                if self.numList[mid] == num:
                    break
                elif self.numList[mid] < num:
                    start = mid+1
                else:
                    end = mid-1
            if self.numList[mid] < num:
                self.numList.insert(mid+1, num)
            else:
                self.numList.insert(mid, num)

    def findMedian(self) -> float:
        length = len(self.numList)
        middle = math.floor(length/2)
        if length == 1:
            return self.numList[0]
        elif length % 2 == 0:
            print()
            return (self.numList[middle-1]+self.numList[middle])/2
        else:
            return self.numList[middle]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
