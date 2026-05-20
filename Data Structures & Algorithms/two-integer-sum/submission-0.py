class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        leny = len(nums)
        for i in range(leny):
            b = target-nums[i]
            if(nums[i] in dic):
                return[dic[nums[i]],i]
            dic[b] = i
        return

            