class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        first = 0
        second = 1
        res = 0
        for i in range(n-1):
            res = first + second
            first = second
            second = res
        return res%1000000007

s = Solution()
print(s.fib(5))