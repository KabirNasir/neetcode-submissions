class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            print(i,nums[i],goal)
            if i + nums[i] >= goal:
                print("goal changed")
                goal = i
        return goal == 0
        