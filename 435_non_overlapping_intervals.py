def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Sorting the interval, then compare the latest chekced item to the next item. 
        If overlap -> pick the one with lower end, and increase res by 1 
        If not -> replace by cur_end 
        '''
        intervals = sorted(intervals, key = lambda x: x[0])
        latest_end = intervals[0][1]
        count = 0 

        for cur_start, cur_end in intervals[1:]:
            # overlap 
            if cur_start < latest_end: 
                latest_end = min(latest_end, cur_end)
                count += 1
            else:
                latest_end = cur_end 
        
        return count
