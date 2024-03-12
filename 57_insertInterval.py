def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            if new_end < cur_start -> it lies between 2 interval -> append to res and return it with the rest of the arr 
            if new_start > cur_end -> larger than current item, append current item to res and move on
            if new_start is not larger than cur_end, and new_end is not is not smaller than cur start -> match -> replace newInterval by merging 2 intervals

            when it doesn't return, it also means that we haven't add newinterval 
        '''

        res = []
        for idx, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[idx:]
            
            elif newInterval[0] > interval[1]:
                res.append(interval)
            
            else:
                newInterval = (
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                )
        
        res.append(newInterval)
        return res
