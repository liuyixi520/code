# 使用集合这个数据结构的特性
# 集合中是不允许重复元素的出现的
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1 = set(nums)
        s2 = set()
        for i in range(len(nums)):
            s2.add(i+1)
        return list(s2-s1)