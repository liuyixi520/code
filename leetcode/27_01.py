# 从后往前便利，碰到目标元素val，就把当前的元素删除掉
# 误区：不能够从前往后删除，删除数组元素后，数组后面的元素会集体向前移动一位
# 从前往后删除，删除元素后，会发生数组越界
# 所以数组中的元素删除和添加都是比较麻烦的，需要考虑数组的越界问题，悲观的估计时间复杂度为O(n)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        if size == 0:
            return 0
        for i in range(size-1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)