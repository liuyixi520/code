# 出现元素最多的那个数字
# 注意前提条件：这个数组是费控的，多数元组是存在的而且个数要大于n/2
# 思路：使用字典这个数据结构，使用key来存储数字，value来存储出现的次数

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 定义一个字典，存储数字和出现的次数
        d = {}
        # 遍历数组
        for num in nums:
            # 如果字典中存在这个数字，则次数加1
            if num in d:
                d[num] += 1
            # 否则初始化为1
            else:
                d[num] = 1
        # 遍历字典，找到出现次数最多的数字
        for key, value in d.items():
            if value > len(nums) / 2:
                return key