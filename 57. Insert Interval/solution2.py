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
        i = 1
        while i < len(intervals):
            first1, first2 = intervals[i-1]
            second1, second2 = intervals[i]

            if first2 >= second1:
                intervals.pop(i)
                intervals[i-1] = [min(first1, second1), max(first2, second2)]
                i -= 1
            i += 1
        return intervals
