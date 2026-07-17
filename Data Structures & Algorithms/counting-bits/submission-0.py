class Solution:
    def countBits(self, n: int) -> List[int]:
        lis=[]
        for nums in range(n+1):
            c =0
            while nums != 0:
                t = nums%2
                if t == 1:
                    c+=1
                nums= nums//2
                
            lis.append(c)
        return lis