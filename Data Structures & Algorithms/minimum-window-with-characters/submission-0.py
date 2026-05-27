class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c1 = {}
        for i in range(len(t)):
            c1[t[i]]=1 + c1.get(t[i],0)
        print (c1)
        l = 0
        strs = ""
        match = 0
        r =0
        window = {}
        minStr = ""
        minStrlen = -1
        for r in range(len(s)):
            print(l,r)
            window[s[r]] = 1 + window.get(s[r], 0)
            if(s[r] in c1 and window[s[r]] == c1[s[r]] ):
                match+=1
            while match == len(c1):
                print(minStr)
                strs = s[l:r+1]
                if minStrlen == -1 or (r - l + 1) < minStrlen:
                    minStr = s[l:r+1]
                    minStrlen = r - l + 1
                window[s[l]] -=1
                if s[l] in c1 and window[s[l]] < c1[s[l]]:
                    match -= 1
                l += 1
        return minStr
        