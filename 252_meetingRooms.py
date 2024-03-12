def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals = sorted(intervals)
        start, end = intervals[0]
        for next_start, next_end in intervals[1:]:
            if next_start >= end or next_end <= start:
                start = min(start, next_start)
                end = max(end, next_end)
            else:
                return False

        return True
