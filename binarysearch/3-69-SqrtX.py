class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        for i in range(1,x):
            if (i+1)*(i+1) > x:
                return i
