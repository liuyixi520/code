# 自顶向下，直接使用暴力递归的方式，注意递归的三个要素
# 1. 递归基
# 2. 要向递归基靠近
# 3. 要自己调用自己
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n==1 or n ==2):
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
s = Solution()
print(s.climbStairs(5))