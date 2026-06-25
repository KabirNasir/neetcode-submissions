class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = {}
        for task in tasks:
            frequencies[task] = frequencies.get(task, 0) + 1

        heap = [-cnt for cnt in frequencies.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue:
            time += 1
            print("time",time)
            if  heap:
                cnt = 1 +heapq.heappop(heap)
                if cnt :
                    queue.append([cnt,time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time