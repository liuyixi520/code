# 这个方法是高斯先想出来的，重点是这个数组要单调递增，不能有重复的数字
# 记找寻的区间为[left, right]

# 还有这里大部分的代码都是copilot写出来的，我只是一个打杂的，哈哈
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        