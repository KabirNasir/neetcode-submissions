class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nl = [x * -1 for x in nums]
        heapq.heapify(nl)  
        for i in range(k-1):
            heapq.heappop(nl)
        return -1*heapq.heappop(nl)

        