# 合并两个有序的数组
# 思路：先将两个数组合并，再排序
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 将两个数组合并
        nums1[m:m+n] = nums2
        # 排序
        nums1.sort()