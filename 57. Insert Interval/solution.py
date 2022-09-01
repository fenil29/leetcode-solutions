class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        startIndex = 0
        ans = []
        while startIndex < len(intervals) and intervals[startIndex][0] < newInterval[0]:
            startIndex += 1
        startIndex -= 1
        intervals.insert(startIndex+1, newInterval)
        for i in intervals:
            self.appendLast(ans, i)
        return ans

    def appendLast(self, numList, num):
        if len(numList) == 0:
            numList.append(num)
        else:
            lastNum = numList[-1]
            if lastNum[1] < num[0]:
                numList.append(num)
            else:
                numList.pop()
                numList.append(
                    [min(num[0], lastNum[0]), max(num[1], lastNum[1])])
