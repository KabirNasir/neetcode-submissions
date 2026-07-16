class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        c =0
        while n != 0:
            t = n%2
            if t == 1:
                c+=1
            n= n//2
            print(n)
        return c


        