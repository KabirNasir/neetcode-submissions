class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canwesplit(largest):
            s = 0
            cs = 0
            for n in nums:
                cs +=n
                if cs > largest:
                    s +=1
                    cs = n
            return s+1<=k
        
        l,r = max(nums),sum(nums)
        res =r
        while l<=r:
            m = (l+r )//2
            if canwesplit(m):
                res =m
                r = m-1
            else:
                l = m+1
        return res
