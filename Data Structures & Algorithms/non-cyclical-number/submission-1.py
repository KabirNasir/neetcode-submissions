class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True :
            digits = []
            s = 0
            while n > 0:
                t= n % 10
                s = s + t ** 2
                n //= 10  
            if(s == 1):
                return True
            if s in seen :
                return False
            seen.add(s)
            n= s
        return False
        