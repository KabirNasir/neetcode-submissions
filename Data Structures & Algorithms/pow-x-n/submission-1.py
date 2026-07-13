class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            half = helper(x*x, n // 2)
            return x * half if n % 2 else half

        result = helper(x, abs(n))
        return result if n >= 0 else 1 / result

        