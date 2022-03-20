# 返回两个数组的交集
# 双指针法
# 分别将两个数组进行排序
# 用两个指针分别指向两个数组的头部
# 如果两个指针指向的数字相等，则将其加入结果数组，然后将两根指针向后移动一位
# 否则，将较小的指针向后移动一位
# 当有一个指针到达数组的末尾时，循环结束
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 将两个数组排序
        nums1.sort()
        nums2.sort()
        # 初始化两个指针，初始化结果数组
        p1 = 0
        p2 = 0
        res = []
        # 循环
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 = p1 + 1
                p2 = p2 + 1
            elif nums1[p1] < nums2[p2]:
                p1 = p1 + 1
            else:
                p2 = p2 + 1
        return res