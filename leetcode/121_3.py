# 买股票的最佳时机
# 想要在第i天获得最大收益，那么必定是在[0, i-1]这个区间里最小的那天买入的
# 因此，采用一个哨兵节点min_price, 我们可以用一个变量min_price来记录这个区间里的最小值
# 同时记最大的收益max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化哨兵节点
        min_price = int(1e9)
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit