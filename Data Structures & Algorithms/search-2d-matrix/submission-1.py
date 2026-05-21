class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        priya = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                priya.append(matrix[i][j])
        print(priya)
        l=0
        r=len(priya)-1
        
        while(l<=r):
            mid = (l+r)//2
            if(target == priya[mid]):
                return True
            elif target > priya[mid]:
                l=mid+1
            else:
                r = mid-1


        return False
        