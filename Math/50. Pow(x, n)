class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1.0

        half_result = self.myPow(x, abs(n)//2)
        result = half_result * half_result

        if abs(n) % 2 == 1:
            result *= x
        
        if n < 0:
            return 1/result
        return result
