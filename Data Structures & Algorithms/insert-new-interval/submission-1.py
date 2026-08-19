class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        i = 0

        while i < len(intervals) and intervals[i][1] < s:
            i += 1

        while i < len(intervals) and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            del intervals[i]

        intervals.insert(i, [s, e])

        return intervals