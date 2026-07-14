class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sety = set()
        for i in nums:
            if i not in sety:
                sety.add(i)
            else:
                sety.remove(i)
        return list(sety)[0]
                