class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def diw(mid):
            cd = 1
            cs =0
            reversed_copy = weights[::-1]
            for i in reversed_copy:
                if  cs +i <= mid:
                    cs +=i
                else:
                    cs =i
                    cd+=1
               
            if(cd <= days):
                return True
            else: return False
        
        R = sum(weights)
        L = max(weights)
        res =R

        while L <=R :
            mid = (L + R) //2 
            if diw(mid):
                
                res = min(res,mid)
                R  = mid-1
            else:
                L = mid+1

        return res
    
    


