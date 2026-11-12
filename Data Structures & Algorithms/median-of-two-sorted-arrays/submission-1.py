class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        maxs = len(nums1)+len(nums2)
        i ,j = 0,0
        s = list()
        while(True):
            if(i == len(nums1) or j == len(nums2)):
                break
            if nums1[i] == nums2[j]:
                s.append(nums1[i])
                s.append(nums2[j])
                i+=1
                j+=1
            elif nums1[i]> nums2[j]:
                s.append(nums2[j])
                j+=1
            else: 
                s.append(nums1[i]) 
                i+=1
        if(i == len(nums1) ):
            s.extend(nums2[j:])
        elif j == len(nums2):
            s.extend(nums1[i:])
       
        print(s)
        if(maxs%2 == 0):
            a =(s[maxs//2] + s[(maxs//2)-1])/2
            print(a,s[maxs//2], )
            return a
        else:
     
            return(s[maxs//2])


