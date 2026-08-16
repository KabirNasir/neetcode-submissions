class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        lenn = (len(s))//2
        print(lenn)

        for i in range(lenn):
            print(s[i],s[j])
            t = s[i]
            s[i] = s[j]
            s[j]=t
            j-=1
        
        