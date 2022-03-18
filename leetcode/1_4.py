# 两数之和，使用哈希表来解决
# key是数组中的元素，value是元素的下标
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 初始化一个字典
        dic = {}
        for i in range(len(nums)):
            # 如果字典中已经有这个数，则返回
            if nums[i] in dic:
                return [dic[nums[i]], i]
            # 如果字典里没有这个数字，那么就把target-nums[i]作为key，i作为value存入字典
            dic[target - nums[i]] = i