# 使用双指针策略，初始化两个指针p1, p2分别指向两个数组的头部，并且用sorted记录结果
# 如果两个指针都没有指向数组的尾部，就一直循环下去
# 如果到了nums1的尾部，就把nums2后面的元素续在结果后面，反之在nums2也是这样做
# 如果nums1[p1]的值比较小，那么就把它插在结果后面，并且将p1后移以为，反之在nums2相同

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in3place instead.
        """
        p1 = 0
        p2 = 0
        res = []
        while p1<m or p2<n:
            if p1==m:
                res.append(nums2[p2])
                p2 = p2 + 1
            elif p2==n:
                res.append(nums1[p1])
                p1 = p1 + 1
            elif nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 = p1 + 1
            else:
                res.append(nums2[p2])
                p2 = p2 + 1
        nums1[:] = res
        
        print(nums1)

s = Solution()
s.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)