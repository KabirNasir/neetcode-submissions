
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l=0
        for r in range(k,len(nums)+1):
            lis = nums[l:r]
            slis = [i * -1 for i in lis]
            heapq.heapify(slis) 
            res.append( -1 * heapq.heappop(slis))
            l=l+1

        return res

        