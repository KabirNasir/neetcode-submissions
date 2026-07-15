class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lenn = len(nums)
        while lenn >= 0:
            if lenn not in nums:
                return lenn
            lenn -= 1

        