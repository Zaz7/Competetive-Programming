
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            symbol = -1
            x *= -1
        else:
            symbol = 1
        
        
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        
        
        reverse *= symbol
        
        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0
        
        return reverse