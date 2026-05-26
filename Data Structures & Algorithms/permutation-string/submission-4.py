class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        if window > len(s2):
            return False
        c1 = [0]*26
        c2 = [0]*26
        
        for i in range(window):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
        
        if c2 == c1:
            return True
        
        l = 0
        for r in range(window, len(s2)):
            # add new character
            c2[ord(s2[r]) - ord('a')] += 1
            # remove left character
            c2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if c2 == c1:
                return True
        
        return False
            



        