# 只遍历数组一次即可
# 假设在第i天卖出股票，那么要想获得最佳利润，一定是[0, i-1]这个区间最低点那天买入的
# 用一个哨兵节点minPrice，用来记录第i天时，[0, i-1]这个区间最低股票的那个价格
# maxProfile用来记录获得的最佳利润
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice = int(1e9)
        maxProfile = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfile = max(maxProfile, price-minPrice)
        return maxProfile
