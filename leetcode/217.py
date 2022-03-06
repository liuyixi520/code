# 使用集合这个数据结构
# 集合中是不允许有重复元素的
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        if len(s) == len(nums):
            return False
        return True