class Solution:
    def find_b(self, a, c):
        val = (c - a**2)**0.5
        if val / int(val) != 1:
            return False
        return True
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        a = 0
        while a **2 < c:
            if self.find_b(a, c):
                return True
            a += 1
        return False