class Solution:
    def findMin(self, nums: List[int]) -> int:
        highest = 0
        l= 0
        r= len(nums)-1

        while(l <= r ):
            mid = (l+r)//2

            if(nums[mid] >= nums[highest]):
                highest = mid
                l=mid+1
                print(highest)
            else:
                r = mid-1
        
        if(highest == len(nums)-1):
            return(nums[0])
        else:
            return(nums[highest+1])
