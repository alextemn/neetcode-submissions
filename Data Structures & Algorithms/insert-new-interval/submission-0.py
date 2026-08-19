class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        res = []
        i = 0
        for start, end in intervals:
            if end < s:
                res.append([start, end])
                i += 1
            elif (end >= s and start <= e) or (start <= e and end >= e):
                s = min(s, start)
                e = max(e, end)
            else:
                res.append([start, end])

        res.insert(i, [s,e])
        return res