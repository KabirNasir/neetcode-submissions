class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        l = 0
        # r = window -1
        sorted_text1 =  "".join(sorted(s1))
        print("sorted_text1",sorted_text1)
        for r in range( window , len(s2)+1):
            print(window,len(s2),r)
            strs = s2[l:r]
            sorted_text2 = "".join(sorted(strs))
            print("sorted_text2",sorted_text2)
            if(sorted_text1 == sorted_text2):
                return True
            l=l+1
        return False
            



        