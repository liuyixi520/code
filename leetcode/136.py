# 只出现一次的数字
# 思路使用数据结构集合set，不允许重复的元素出现的原理

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 将数组转换成集合
        s = set(nums)
        # 求集合中的元素和
        return sum(s) * 2 - sum(nums)