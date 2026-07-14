class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        if rev not in range(-2**31,2**31-1):return 0
        if x>=0: return rev
        if x<0: return -(rev)



        