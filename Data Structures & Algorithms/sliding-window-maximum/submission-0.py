
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        # res = nums[l:k]
        dq = deque()
        highest = {}
        for r in range(len(nums)):
            dq.append(nums[r])
            if(len(dq) == k):
               
                sdq = deque(sorted(dq)) 
                
                res.append(sdq.pop())
                dq.popleft()
                # print(dq)
        return res

        