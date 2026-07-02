class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] <9 :
            digits[-1]+=1
            return digits
        else :
            sumi=0
            for i in digits:
                sumi = sumi*10+ i

            sumi = sumi+1
            shelf=[]
            while sumi>0:
                t = sumi%10
                shelf.insert(0,t)
                sumi=sumi//10
            return shelf
                







        