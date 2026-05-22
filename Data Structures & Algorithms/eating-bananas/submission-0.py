class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = right

        while left <= right:
            speed = (left + right) // 2
            hours_needed = 0

            for bananas in piles:
                hours_needed += math.ceil(bananas / speed)

            if hours_needed <= h:
                answer = speed
                right = speed - 1
            else:
                left = speed + 1

        return answer