import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        num_digits = math.floor(math.log10(x)) + 1
        digits = [(x % 10 ** i) // 10 ** (i - 1) for i in range(1, num_digits + 1)]
        return digits == list(reversed(digits))
