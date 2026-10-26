class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def sumdi(arr, d):
            s =0
            for i in arr:
                if(i%d == 0):
                    s = s + (i//d)

                else :
                    s = s+ (int)(i//d) + 1
          
            return s
        arr = list()
        maxx = 0
        for i in range(len(piles)):
            maxx = max(maxx,piles[i])
        l= 1
        r = maxx
        mind= 0
        while(l<=r):
            mid = (l+r)//2
            np = sumdi(piles, mid)
            if np <= h:
                mind = mid
                r= mid -1     
            elif np > h:
                l =mid+1
        return mind




        

        