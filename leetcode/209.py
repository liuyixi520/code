# 暴力法：穷举所有的情况，然后判断是否符合条件
# 时间复杂度：O(n^2)
# 返回最小的那个数
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        if size==0:
            return 0
        # 最大的长度不会超过数组的长度
        res = size+1
        # i表示当前子数组的起始位置，j表示当前子数组的结束位置
        for i in range(size):
            sum = 0
            for j in range(i, size):
                sum += nums[j]
                if sum >= target:
                    res = min(res, j-i+1)
                    break
        if res == size+1:
            return 0
        return res