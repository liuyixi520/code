# 使用一个hashmap，用来记录原来数组中的元素
# 类似使用set的方法，使用差异性，找出来消失的数字
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s = set(nums)
        res = []
        for i in range(len(nums)):
            if i+1 not in s:
                res.append(i+1)
        return res