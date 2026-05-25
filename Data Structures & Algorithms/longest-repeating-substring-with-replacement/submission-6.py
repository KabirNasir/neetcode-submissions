class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hashmap for counting freq
        res = 0
        l=0
        length = len(s)
        maxf = 0
        for r in range(length) :
            count[s[r]]=1 + count.get(s[r],0)
            #soln 3 with maxf(really optimized)

            maxf = max(maxf, count[s[r]])
            # reduces runtime from o(26n) to o (n)
            while ((r-l+1) - maxf > k ):
                count[s[l]] -=1
                l+=1

            res = max(res, (r-l+1))
        return res