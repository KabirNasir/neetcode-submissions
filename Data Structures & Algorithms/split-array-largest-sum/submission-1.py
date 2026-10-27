class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        res =[]
        def bt(start, groups):

            if(len(groups) == k):
                if(len(nums) == start):

                    res.append(groups)
                return
            

            for e in range(start+1 , len(nums)+1):
                g = nums[start:e]
                bt(e, groups + [g])
        
        bt(0,[])

        mind = math.inf
        for i in range(len(res)):
            m= 0
            for s in range(k):
                m = max(m,sum(res[i][s]))
            mind = min(mind,m)    
        return mind
