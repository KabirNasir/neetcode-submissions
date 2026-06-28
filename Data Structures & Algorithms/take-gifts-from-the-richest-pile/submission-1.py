import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        i = 0
        while(i<k):
            gifts.sort()
            a = gifts[-1]
            a = math.floor(math.sqrt(a))
            gifts[-1] = a
            # print(gifts)
            i+=1
        return sum(gifts)

        