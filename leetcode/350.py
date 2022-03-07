# 使用双指针策略
# 将两个数组分别排序，比较两根指针上值的大小
# 如果两个值相等，那么就往结果集里放，同时两根指针都往后走
# 否则较小那根指针往后走
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        len1 = len(nums1)
        len2 = len(nums2)
        res = []
        p1, p2 = 0, 0
        nums1.sort()
        nums2.sort()
        while p1 < len1 or p2 < len2:
            if p1==len1:
                break
            elif p2==len2:
                break
            elif nums1[p1]==nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1]<nums2[p2]:
                p1 += 1
            elif nums1[p1]>nums2[p2]:
                p2 += 1
        return res
                

s = Solution()
print(s.intersect([1,2,2,1], [2,2,1]))