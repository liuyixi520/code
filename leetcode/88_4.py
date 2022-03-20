# 合并两个有序的数组
# 策略：使用双指针，一个指针指向第一个数组，一个指针指向第二个数组
# 把较小的数字放到新数组中
# 时间复杂度：O(m+n)
# 空间复杂度：O(1)
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in3place instead.
        """
        # 先把nums1中后面多余的0清空
        nums1[m:] = []
        # 初始化两个指针和结果
        p1 = 0
        p2 = 0
        res = []
        # 循环
        while p1<m and p2<n:
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 = p1 + 1
            else:
                res.append(nums2[p2])
                p2 = p2 + 1
        # 把剩余的数字放到结果中
        res.extend(nums1[p1:])
        res.extend(nums2[p2:])
        # 把结果赋值给nums1
        nums1[:] = res

