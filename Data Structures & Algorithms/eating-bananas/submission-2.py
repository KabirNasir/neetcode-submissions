class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while(l <= r):
            mid = (l+r)//2
            hrs=0
            for bananas in piles:
                hrs = hrs + math.ceil(bananas/mid)
            if(hrs <= h):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans