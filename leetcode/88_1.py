# 将nums1数组的后半部分切出来，直接用nums2续上
# 用list自带的sort()函数对新数组进行排序即可
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in3place instead.
        """
        nums1[m:] = nums2
        nums1.sort()