def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        a heap: store tasks with its counting
        a queue: store waiting tasks 
        whenever heap and queue is empty, then we're done and return units
        """

        units = 0
        heap = [(-count, task) for task, count in Counter(tasks).items()]
        heapq.heapify(heap)
        queue = []

        while heap or queue:
            # Cooldown the tasks in queue
            queue = [(cooldown-1, count, task) for cooldown, count, task in queue]
            
            # Get the next tasks in line 
            item = heapq.heappop(heap) if heap else None
            
            # Add to queue after execute the curr task
            if item:
                curr_count, curr_task = item
                if curr_count + 1 < 0: queue.append((n, curr_count+1, curr_task))
            
            # If the last recent task is done cooldown, then add it to heap
            if queue and queue[0][0] == 0:
                _, new_count, new_task = queue[0]
                queue = queue[1:]
                heapq.heappush(heap, (new_count, new_task))

            units += 1 
        
        return units
