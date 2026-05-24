class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        maxl = max(l1,l2)
        minl = min(l1,l2)
        lis = []
        c1 ,c2 = 0,0
        
        while(True):
            if(c1 == l1):
                lis.extend(nums2[c2:])
                break
            elif(c2 == l2):
                lis.extend(nums1[c1:])
                break

            
            if(nums1[c1] < nums2[c2]):
                lis.append(nums1[c1])
                c1+=1
            else:
                lis.append(nums2[c2])
                c2+=1
        l3 = len(lis)
        if(l3 % 2 == 0):
            value = (int)((l3/2) - 1)

            median = (lis[value] + lis[value+1])
            median = median/2
            return median
        else:
            return lis[l3//2]
        


