# 动态规划
# 最大子数组最后的那个数字必定在元数组中，所以按照这个思路遍历原来的数组
# 转移方程是：pre = max(pre+nums[i], nums[i])
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # 当前节点可以取到的最大值
        pre = 0
        # 记录遍历过程中最大的值
        maxAns = nums[0]
        for i in range(n):
            pre = max(pre+nums[i], nums[i])
            maxAns = max(pre, maxAns)
        return maxAns