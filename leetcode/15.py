# 三数之和
# 将这个问题转换成两数之和问题，可以使用哈希表来解决这个问题。

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 定义一个空列表，用来存储结果
        res = []
        # 先遍历这个数组，用来去除当前第一个元素，那么剩下的两个元素就是我们要找的两个数字
        # 由于题目中不允许有重复元素，那么剩下的两个数组必然在后面的数字中
        for i in range(len(nums)):
            target = -nums[i]
            # 遍历剩下的数组，转换成两数之和问题
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    # 如果两数之和等于target，则将这个结果加入列表
                    if nums[j] + nums[k] == target:
                        res.append([nums[i], nums[j], nums[k]])
        # 返回结果
        return res