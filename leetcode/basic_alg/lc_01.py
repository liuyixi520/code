class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 如果正向来，删除之后，数组的长度会变短，进而造成最后的数组访问越界
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] == nums[i]:
                del nums[i]