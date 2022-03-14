# 第一步：将数组里的元素都平方
# 第二步：将数组里的元素排序
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [i**2 for i in nums]
        res.sort()
        return res