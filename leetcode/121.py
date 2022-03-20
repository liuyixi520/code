# 买股票的最佳时机
# 暴力法
# 穷举出来所有的情况，然后比较最大的
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # i代表买入的时候的索引
        for i in range(len(prices)):
            # j代表卖出时候的索引
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit