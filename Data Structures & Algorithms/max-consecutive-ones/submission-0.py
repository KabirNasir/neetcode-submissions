class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        c =0
        for i in nums:
            if i ==1:
                c+=1
                maxi=max(c,maxi)
            if i == 0:
                c=0
        return maxi

        