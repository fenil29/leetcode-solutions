class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda num: num[0])
        i = 1
        ans = 0
        _, end = intervals[0]
        while i < len(intervals):
            second1, second2 = intervals[i]
            if end > second1:
                end = min(second2, end)
                ans += 1
            else:
                end = second2
            i += 1
        return ans
