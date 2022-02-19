#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型
#
# 采用方法：使用动态规划
# 状态定义：声明一个数组dp[i]，用来记录以array[i]结尾的最大子数组和
# 状态转移方程：如果dp[i-1]大于零，那么dp[i] = dp[i-1]+array[i]
#            反之dp[i]<=0，那么dp[i] = array[i]，综上转移方程为：
#            dp[i] = max(arrayp[i], dp[i-1]+array[i])
# 初始化：dp[0] = array[0]
class Solution:
    def FindGreatestSumOfSubArray(self , array: list[int]) -> int:
        # write code here
        dp = [i for i in range(len(array))]
        dp[0] = array[0]
        res = dp[0]
        for i in range(1, len(array)):
            dp[i] = max(dp[i-1]+array[i], array[i])
            res = max(res, dp[i])
        return res
sol = Solution()
lst = [1,-2,3,10,-4,7,2,-5]
print(sol.FindGreatestSumOfSubArray(lst))