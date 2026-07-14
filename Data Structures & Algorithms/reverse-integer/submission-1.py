class Solution:
    def reverse(self, x: int) -> int:
        absX = abs(x)
        y = str(absX)
        rev = int(y[::-1])
        if x>=0:
            if  rev in range(-2**31,2**31-1):
                return rev
            else:
                return 0
        
        if x<0:
            if  rev in range(-2**31,2**31-1):
                return -(rev)
            else:
                return 0


        