# 巧用数组下标，数组的下标刚好存放的是连续区间[0, n)
# 迭代原来的数组，数组中的每个元素记作num
# 使用(num-1)%n，找到这个数字所代表的下标
# 这里为什么要取n的模？因为数字会重复，所以n会被叠加多次，所以取一下模
# 然后将这个下标对应的值+n，就表示这个下标的值已经出现了，就不是没出现的元素 
# 然后便利整个数组，凡是大于n的元素下标都是在出现过的数字 

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for num in nums:
            # 下标是从0开始的，数组中的元素是从1开始的
            x = (num-1)%n
            nums[x] += n
        res = [i+1 for i,num in enumerate(nums) if num<=n]
        return res