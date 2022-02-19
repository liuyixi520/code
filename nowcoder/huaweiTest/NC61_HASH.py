#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @param target int整型 
# @return int整型一维数组
# 备注：采用哈希表的方法


class Solution:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        hashtable = dict()
        res = []
        for i, num in enumerate(numbers):
            sub = target - num
            if sub in hashtable:
                res = [hashtable[sub]+1, i+1]
                res.sort()
                return res
            hashtable[num] = i