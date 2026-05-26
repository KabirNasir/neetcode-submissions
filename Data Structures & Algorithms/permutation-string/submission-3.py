class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        l = 0
        # r = window -1
        # sorted_text1 =  "".join(sorted(s1))
        c1 = [0]*26
        # print("sorted_text1",sorted_text1)
        for i in s1:
            c1[ord(i) - ord('a')] += 1
        for r in range( window , len(s2)+1):
            # print(window,len(s2),r)
            c2 = [0]*26
            strs = s2[l:r]
            # sorted_text2 = "".join(sorted(strs))
            for i in strs:
                c2[ord(i) - ord('a')] += 1
            # print("sorted_text2",sorted_text2)
            if(c1 == c2):
                return True
            l=l+1
        return False
            



        