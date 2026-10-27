class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        ans = float('inf')

        def bt(start, groups):
            nonlocal ans

            if len(groups) == k:
                if start == len(nums):
                    largest = max(sum(g) for g in groups)
                    ans = min(ans, largest)
                return

            for e in range(start + 1, len(nums) + 1):
                g = nums[start:e]
                bt(e, groups + [g])

        bt(0, [])
        return ans