from typing import List
from operator import itemgetter
from heapq import heappush, heappop

# Way1: use sort and priority queue
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(0))

        min_heap_of_end = []
        needed_rooms = 0
        max_needed_rooms = 0
        for interval in intervals:
            start, end = interval[0], interval[1]

            while len(min_heap_of_end) > 0:
                lowest_end = heappop(min_heap_of_end)
                if lowest_end <= start:
                    needed_rooms -= 1
                else:
                    heappush(min_heap_of_end, lowest_end)
                    break

            heappush(min_heap_of_end, end)
            needed_rooms += 1

            max_needed_rooms = max(max_needed_rooms, needed_rooms)
        
        return max_needed_rooms

# Way2: only care sorted start and end
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_min_heap, end_min_heap = [], []

        for interval in intervals:
            start, end = interval[0], interval[1]

            heappush(start_min_heap, start)
            heappush(end_min_heap, end)

        needed_rooms = 0
        max_needed_rooms = 0
        while len(start_min_heap) > 0:
            end = heappop(end_min_heap)

            while True:
                if len(start_min_heap) == 0:
                    break

                start = heappop(start_min_heap)
                if start < end:
                    needed_rooms += 1
                    max_needed_rooms = max(max_needed_rooms, needed_rooms)
                else:
                    needed_rooms -= 1
                    heappush(start_min_heap, start)
                    break

        return max_needed_rooms

if __name__ == '__main__':
    assert Solution().minMeetingRooms([[5, 10],[0, 30],[15, 20]]) == 2
    assert Solution().minMeetingRooms([[1, 2]]) == 1
    assert Solution().minMeetingRooms([[7,10],[2,4]]) == 1