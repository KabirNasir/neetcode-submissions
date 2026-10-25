class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = [ 0,0,0]
        for i in range(len(nums)):
            c[nums[i]]+=1
        i = 0
        for n in range(len(c)):
            for j in range(c[n]):
                nums[i]= n
                i+=1
        return nums

