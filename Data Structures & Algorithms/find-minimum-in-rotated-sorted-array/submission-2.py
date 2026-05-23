class Solution:
    def findMin(self, nums: List[int]) -> int:
        l= 0
        r= len(nums)-1

        while(l <= r ):
            mid = (l+r)//2

            if(nums[mid] >= nums[r]):
                highest = mid
                l=mid+1
                print(highest)
            else:
                r = mid
        print(nums[r])
        return nums[r]
