class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hashmap for counting freq
        res = 0
        l=0
        length = len(s)
        for r in range(length) :
            count[s[r]]=1 + count.get(s[r],0)
            #soln 2 with if 
            while ((r-l+1) - max(count.values())) > k :
                count[s[l]] -=1
                l+=1

            res = max(res, (r-l+1))
        return res