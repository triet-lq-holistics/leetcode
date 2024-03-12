import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
            1 room is taken and reset new end time
            the other room turns out to be has lower end time
            how do store end time

            using heap
        '''

        # Sort and store the end time of the first meeting
        intervals = sorted(intervals)

        # Compare with the last interval, if overlap then count 1. Replace the end time by maximum between the 2 end times
        heap = []
        heapq.heappush(heap, intervals[0][1])
        
        count = 1
        for idx in range(1, len(intervals)):
            cur_start, cur_end = intervals[idx]
            if cur_start < heap[0]: 
                count += 1
                heapq.heappush(heap, cur_end)
            else: 
                heapq.heappop(heap)
                heapq.heappush(heap, cur_end)
        
        return count
