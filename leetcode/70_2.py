# 自下到顶，使用循环的方式
class Solution:
    def climbStairs(self, n: int) -> int:
        # 初始化第一个楼梯
        first = 1
        # 初始化第二个楼梯
        second = 2
        res = 0
        if(n<=2):
            return n
        for i in range(n-2):
            res = first + second
            first = second
            second = res
        return res
s = Solution()
print(s.climbStairs(5))