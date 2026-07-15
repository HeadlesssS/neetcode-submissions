class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>=0 else -1
        num = abs(x)
        rev = 0
        while num> 0:
            rev = rev * 10 + (num % 10)

            num= num//10
            print(f"nums{num}")

            print(rev)
        
        if rev in range(-2**31,2**31-1):
            return sign * rev
        
        return 0







        