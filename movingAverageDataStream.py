"""Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]
Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3"""

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def _push(self, val):
        if len(self.queue) >= 3:
            self.queue = self.queue[1:]
        self.queue.append(val)
    
    def next(self, val):
        self._push(val)
        return sum(self.queue) / len(self.queue)


movingAverage  = MovingAverage(3)
print(movingAverage.next(1)) # return 1.0 = 1 / 1
print(movingAverage.next(10)) # return 5.5 = (1 + 10) / 2
print(movingAverage.next(3)) # return 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5)) # return 6.0 = (10 + 3 + 5) / 3