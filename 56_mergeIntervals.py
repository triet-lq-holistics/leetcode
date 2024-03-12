 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        
        mergedInterval = intervals[0]
        res = []

        for interval in intervals[1:]:
            if mergedInterval[1] >= interval[0]:
                mergedInterval = [mergedInterval[0], max(mergedInterval[1], interval[1])]
            else:
                res.append(mergedInterval)
                mergedInterval = interval
        res.append(mergedInterval)
        return res
