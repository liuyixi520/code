# 暴力穷举法，穷举出来所有可能的收益
# 思路是对的，但是超时了
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i+1, n):
                res = max(res, prices[j] - prices[i])
        return res
