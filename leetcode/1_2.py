class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        # 由于在hashtable中的查找便利是线性的，python中的字典可以当成哈希表使用
        # 这个哈希表中的key是当前元素的值，value是当前元素的下标
        # 便利原来的数组，记当前的元素为num
        # 如果target - num在哈希表中，那么就直接返回即可
        # 如果没有在哈希表中，那么就把当前的值和下标放在key和value中
        for i,num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i