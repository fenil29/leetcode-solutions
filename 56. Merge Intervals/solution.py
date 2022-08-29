class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda num: num[0])
        ans = [intervals[0]]
        for i in intervals[1:]:
            one1, two1 = ans[-1]
            one2, two2 = i
            if two1 >= one2:
                ans.pop()
                ans.append([min(one1, one2), max(two1, two2)])
            else:
                ans.append(i)
        return ans
