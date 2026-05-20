class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r= len(heights)-1
        largest = 0
        length = len(heights)
        while(l!=r) :
            area = (r - l) * min(heights[l],heights[r])
            largest = max(area,largest)
            if(heights[r] >= heights[l] ):
                l+=1
            else:
                r-=1
        
        return largest

            